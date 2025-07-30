from data.display import tampilkan_header, tampilkan_data, tampilkan_tidak_ditemukan, slow_print, YELLOW, RED, RESET
from data.api_client import cari_mahasiswa
import time

def main():
    tampilkan_header()
    try:
        nama = input(f"{YELLOW}[?]{RESET} Masukkan Nama Lengkap Mahasiswa: ").strip()
        if not nama:
            print(f"\n{RED}[x] Nama tidak boleh kosong.{RESET}")
            return

        print(f"\n{YELLOW}[•]{RESET} Mencari data mahasiswa...")
        time.sleep(0.8)

        data = cari_mahasiswa(nama)

        if data:
            time.sleep(0.5)
            tampilkan_data(data)
        else:
            tampilkan_tidak_ditemukan()

    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] Dibatalkan oleh pengguna.{RESET}")

if __name__ == "__main__":
    main()
