import os
import ftplib
import paramiko
import threading
from concurrent.futures import ThreadPoolExecutor
from ssl import create_default_context
from colorama import Fore

# Ensure output folder exists
def ensure_output_folder():
    os.makedirs("output", exist_ok=True)

# TLS initialization for FTP
def initialize_tls():
    context = create_default_context()
    return context

# FTP check function
def check_ftp(line, ftp_counter_lock, ftp_counter, print_lock):
    try:
        host, username, password = line.strip().split()
        context = initialize_tls()

        with print_lock:
            print(f"[ FTP PROSES ] {host}|{username}|{password}")

        ftp = ftplib.FTP_TLS(context=context)
        ftp.connect(host, timeout=20)
        ftp.login(username, password)
        ftp.prot_p()

        directories = ftp.nlst()

        with ftp_counter_lock:
            current_ftp_counter = ftp_counter[0]
            ftp_counter[0] += 1

        with print_lock:
            print(f"{Fore.GREEN}[ FTP SUCCESS ]{Fore.RESET} {host}|{username}|{password}")
        
        output_path = 'output/FTPFound.txt'
        with open(output_path, 'a') as result:
            result.write(f"{current_ftp_counter}. {host}|{username}|{password} - Directories: {', '.join(directories)}\n")
        
        ftp.quit()

    except ftplib.error_perm as e:
        with print_lock:
            print(f"{Fore.RED}[ FTP FAILED ]{Fore.RESET} {host}|{username}|{password} - {e}")
    except ftplib.all_errors as e:
        with print_lock:
            print(f"{Fore.RED}[ FTP FAILED ]{Fore.RESET} {host}|{username}|{password} - {e}")

# SSH check function
def check_ssh(line, ssh_counter_lock, ssh_counter, print_lock):
    try:
        host, username, password = line.strip().split()

        with print_lock:
            print(f"[ SSH PROSES ] {host}|{username}|{password}")

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=22, username=username, password=password, timeout=20)

        sftp = ssh.open_sftp()
        directories = sftp.listdir()

        with ssh_counter_lock:
            current_ssh_counter = ssh_counter[0]
            ssh_counter[0] += 1

        with print_lock:
            print(f"{Fore.GREEN}[ SSH SUCCESS ]{Fore.RESET} {host}|{username}|{password}")
        
        output_path = 'output/SFTPFound.txt'
        with open(output_path, 'a') as result:
            result.write(f"{current_ssh_counter}. {host}|{username}|{password} - Directories: {', '.join(directories)}\n")

        sftp.close()
        ssh.close()

    except paramiko.AuthenticationException:
        with print_lock:
            print(f"{Fore.RED}[ SSH FAILED ]{Fore.RESET} {host}|{username}|{password} - Authentication Failed")
    except paramiko.SSHException as e:
        pass
    except paramiko.socket.error as e:
        with print_lock:
            print(f"{Fore.RED}[ SSH FAILED ]{Fore.RESET} {host}|{username}|{password} - Socket error")

# Process FTP & SSH for the file
def process_ftp_ssh(file_name, max_workers):
    ensure_output_folder()

    # Read login data from the file
    try:
        with open(file_name, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        with open(file_name, 'r', encoding='ISO-8859-1') as f:
            lines = f.readlines()

    # Create locks and counters
    ftp_counter_lock = threading.Lock()
    ssh_counter_lock = threading.Lock()
    print_lock = threading.Lock()
    ftp_counter = [1]
    ssh_counter = [1]

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for line in lines:
            executor.submit(check_ftp, line, ftp_counter_lock, ftp_counter, print_lock)
            executor.submit(check_ssh, line, ssh_counter_lock, ssh_counter, print_lock)
