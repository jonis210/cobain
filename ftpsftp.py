import os
import threading
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init

# Ensure output folder exists
def ensure_output_folder():
    os.makedirs("output", exist_ok=True)

# Display combined ASCII art (you can adjust this to match your actual art)
def display_combined_ascii_art():
    print("Some ASCII Art Here!")  # Replace with your actual ASCII art

# Assuming the function to load FTP and SSH checks is in ftpsftp.py
import ftpsftp  # This will import the validation functions (check_ftp, check_ssh)

# Function to process filter (example placeholder)
def process_filter(file_name, max_workers):
    print(f"[INFO] Processing filter for file: {file_name}")
    # Add actual filter processing logic here

# Function to process Cpanel & WHM (example placeholder)
def process_cpanel_whm(file_name, max_workers):
    print(f"[INFO] Processing Cpanel & WHM for file: {file_name}")
    # Add actual Cpanel & WHM processing logic here

# Function to process WordPress (example placeholder)
def process_wordpress(file_name, max_workers):
    print(f"[INFO] Processing WordPress for file: {file_name}")
    # Add actual WordPress processing logic here

# Function to process VPS login (example placeholder)
def process_vps(file_name, max_workers):
    print(f"[INFO] Processing VPS for file: {file_name}")
    # Add actual VPS login processing logic here

# Function to process RDP login (example placeholder)
def process_rdp(file_name, max_workers):
    print(f"[INFO] Processing RDP for file: {file_name}")
    # Add actual RDP login processing logic here

def main():
    # Ensure the output folder exists
    ensure_output_folder()

    # Display ASCII art
    display_combined_ascii_art()

    print(f"{Fore.RED}[INFO]{Style.RESET_ALL} Mengambil token dari server...")

    # Loop until a valid token is retrieved and decrypted
    while True:
        # Ask for the key input
        key_input = input("[INFO] Masukkan Key: ").strip()

        # Assuming you have a function to get the GitHub token (or just for the demo)
        github_token = "demo-token"  # Replace with actual token-fetching logic

        # If the token retrieval was successful, break the loop
        if github_token:
            break
        else:
            print("[ERROR] Gagal mengambil atau mendekripsi token. Silakan coba lagi.")
    
    # Ask for file name input
    file_name = input(f"{Fore.CYAN}Masukkan nama file login (misal: filter.txt):{Style.RESET_ALL} ").strip()

    # Validate if the file exists
    if not os.path.exists(file_name):
        print(f"[ERROR] File {file_name} tidak ditemukan.")
        return
    else:
        print(f"[INFO] File {file_name} ditemukan dan siap diproses.")
    
    print(f"{Fore.CYAN}Pilih validasi login:")
    
    # List of options for login types
    options = [
        ("Filter url,user,pass", "https://raw.githubusercontent.com/jonis210/loginbaru1/main/filter.py"),
        ("FTP & SSH", "https://raw.githubusercontent.com/jonis210/loginbaru1/main/ftpsftp.py"),
        ("Cpanel & WHM", "https://raw.githubusercontent.com/jonis210/loginbaru1/main/cpwhm.py"),
        ("WordPress", "https://raw.githubusercontent.com/jonis210/loginbaru1/main/wordpress.py"),
        ("VPS", "https://raw.githubusercontent.com/jonis210/loginbaru1/main/vps.py"),
        ("RDP", "https://raw.githubusercontent.com/jonis210/loginbaru1/main/rdp.py"),
    ]

    for idx, (name, _) in enumerate(options, 1):
        print(f"{idx}. {name}")
    
    try:
        choice = int(input(f"{Fore.CYAN}Masukkan nomor pilihan (1, 2, 3, ...):{Style.RESET_ALL} "))
        
        if choice == 1:  # Filter
            print("[INFO] Memproses Filter...")
            # Ask for the number of workers
            max_workers = int(input("[INFO] Masukkan jumlah max worker (contoh: 50): "))
            if max_workers <= 0:
                print("[ERROR] Jumlah max worker harus lebih besar dari 0.")
                return
            
            # Use ThreadPoolExecutor to process Filter
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                # Pass the file name to filter processing function
                executor.submit(process_filter, file_name, max_workers)
        
        elif choice == 2:  # FTP & SSH
            print("[INFO] Memproses FTP dan SSH...")
            # Ask for the number of workers
            max_workers = int(input("[INFO] Masukkan jumlah max worker (contoh: 50): "))
            if max_workers <= 0:
                print("[ERROR] Jumlah max worker harus lebih besar dari 0.")
                return
            
            # Use ThreadPoolExecutor to process FTP and SSH
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                # Pass the file name to FTP and SSH processing function
                executor.submit(ftpsftp.process_ftp_ssh, file_name, max_workers)
        
        elif choice == 3:  # Cpanel & WHM
            print("[INFO] Memproses Cpanel dan WHM...")
            # Ask for the number of workers
            max_workers = int(input("[INFO] Masukkan jumlah max worker (contoh: 50): "))
            if max_workers <= 0:
                print("[ERROR] Jumlah max worker harus lebih besar dari 0.")
                return
            
            # Use ThreadPoolExecutor to process Cpanel & WHM
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                executor.submit(process_cpanel_whm, file_name, max_workers)
        
        elif choice == 4:  # WordPress
            print("[INFO] Memproses WordPress...")
            # Ask for the number of workers
            max_workers = int(input("[INFO] Masukkan jumlah max worker (contoh: 50): "))
            if max_workers <= 0:
                print("[ERROR] Jumlah max worker harus lebih besar dari 0.")
                return
            
            # Use ThreadPoolExecutor to process WordPress
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                executor.submit(process_wordpress, file_name, max_workers)
        
        elif choice == 5:  # VPS
            print("[INFO] Memproses VPS...")
            # Ask for the number of workers
            max_workers = int(input("[INFO] Masukkan jumlah max worker (contoh: 50): "))
            if max_workers <= 0:
                print("[ERROR] Jumlah max worker harus lebih besar dari 0.")
                return
            
            # Use ThreadPoolExecutor to process VPS
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                executor.submit(process_vps, file_name, max_workers)
        
        elif choice == 6:  # RDP
            print("[INFO] Memproses RDP...")
            # Ask for the number of workers
            max_workers = int(input("[INFO] Masukkan jumlah max worker (contoh: 50): "))
            if max_workers <= 0:
                print("[ERROR] Jumlah max worker harus lebih besar dari 0.")
                return
            
            # Use ThreadPoolExecutor to process RDP
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                executor.submit(process_rdp, file_name, max_workers)
        
        else:
            print("[ERROR] Pilihan tidak valid.")
            return

    except ValueError as e:
        print(f"[ERROR] Input tidak valid. Masukkan angka yang benar. Error: {e}")
        return
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {e}")
        return

if __name__ == "__main__":
    main()
