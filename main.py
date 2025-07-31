import time
import sys

# Warn if running under wrong Python version
if sys.version_info.major < 3:
    print("\n\033[91m[!] ERROR: You are running this script with Python 2.\033[0m")
    print("    Please run it using: \033[93mpython3 main.py\033[0m\n")
    sys.exit(1)
elif sys.version_info < (3, 6):
    print("\n\033[91m[!] ERROR: Your Python version is too old.\033[0m")
    print("    This program requires Python 3.6 or newer.")
    print("    Please run it using: \033[93mpython3 main.py\033[0m\n")
    sys.exit(1)

# Check for missing dependencies
required_modules = ["data.display", "data.api_client"]
missing_modules = []

for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        missing_modules.append(module)

if missing_modules:
    print("\n\033[91m[!] Missing required dependencies.\033[0m")
    print("    Please install them by running:")
    print("    \033[93mpip install -r requirements.txt\033[0m\n")
    sys.exit(1)

# Safe to import now
from data.display import tampilkan_header, tampilkan_data, tampilkan_tidak_ditemukan, YELLOW, RED, RESET
from data.api_client import cari_mahasiswa

def main():
    tampilkan_header()
    try:
        nama = input(f"{YELLOW}[?]{RESET} Enter the Full Name of the Student: ").strip()
        if not nama:
            print(f"\n{RED}[x] Name cannot be empty.{RESET}")
            return

        print(f"\n{YELLOW}[•]{RESET} Searching for student data...")
        time.sleep(0.8)

        data = cari_mahasiswa(nama)

        if data:
            time.sleep(0.5)
            tampilkan_data(data)
        else:
            tampilkan_tidak_ditemukan()

    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] Operation canceled by user.{RESET}")

if __name__ == "__main__":
    main()
