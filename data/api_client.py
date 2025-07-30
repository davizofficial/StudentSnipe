from pddiktipy import api

def cari_mahasiswa(nama):
    try:
        client = api()
        hasil = client.search_mahasiswa(nama)
        
        if not hasil or len(hasil) == 0:
            return None
        
        # Ambil mahasiswa pertama dari hasil pencarian
        mhs = hasil[0]

        return {
            "Nama": mhs.get("nama", "-"),
            "NIM": mhs.get("nim", "-"),
            "Program Studi": mhs.get("nama_prodi", "-") or mhs.get("prodi", "-"),
            "Perguruan Tinggi": mhs.get("nama_pt", "-") or mhs.get("pt", "-"),
            "Status": mhs.get("status_mahasiswa", "-"),
            "Angkatan": mhs.get("angkatan", "-")
        }

    except Exception as e:
        print(f"\n⚠️ Gagal ambil data melalui pddiktipy: {e}")
        return None
