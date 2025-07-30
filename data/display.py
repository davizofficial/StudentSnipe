import time
import os

# ANSI escape code untuk warna
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def tampilkan_header():
    clear_screen()
    banner = f"""{CYAN}


                                      ____    _     __     _    ____
                                     |####`--|#|---|##|---|#|--'##|#|
   _                                 |____,--|#|---|##|---|#|--.__|_|
 _|#)_____________________________________,--'EEEEEEEEEEEEEE'_=-.
((_____((_________________________,--------[JW](___(____(____(_==)        _________
                               .--|##,----o  o  o  o  o  o  o__|/`---,-,-'=========`=+==.
                               |##|_Y__,__.-._,__,  __,-.___/ J \ .----.#############|##|
                               |##|              `-.|#|##|#|`===l##\   _\############|##|
                              =======-===l          |_|__|_|     \##`-"__,=======.###|##|
                                                                  \__,"          '======'

     Doxing Student Indonesian Campus

DISCLAIMER: This tool is for educational use only. I do not promote cybercrime or misuse.\n Use it responsibly for learning and ethical research only.
    --------------------------------{RESET}
"""
    print(banner)
    slow_print(f"{YELLOW}[•] Initializing scanner...", 0.03)
    time.sleep(0.5)
    slow_print(f"{YELLOW}[•] Ready to search student data\n", 0.02)

def tampilkan_data(data):
    print(f"{GREEN}[+] Data Mahasiswa Ditemukan:\n{RESET}")
    print("-" * 50)
    for key, value in data.items():
        print(f"{CYAN}{key:<20}:{RESET} {value}")
    print("-" * 50)

def tampilkan_tidak_ditemukan():
    print(f"\n{RED}[-] Data mahasiswa tidak ditemukan atau tidak terdaftar.{RESET}")
