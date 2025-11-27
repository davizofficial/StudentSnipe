from pddiktipy import api

def format_mahasiswa_data(mhs):
    """Format data mahasiswa ke dictionary standar"""
    return {
        "Nama": mhs.get("nama", "-"),
        "NIM": mhs.get("nim", "-"),
        "Program Studi": mhs.get("nama_prodi", "-") or mhs.get("prodi", "-"),
        "Perguruan Tinggi": mhs.get("nama_pt", "-") or mhs.get("pt", "-"),
        "Status": mhs.get("status_mahasiswa", "-"),
        "Angkatan": mhs.get("angkatan", "-")
    }

def cari_mahasiswa(nama, return_all=False):
    """
    Cari mahasiswa berdasarkan nama
    
    Args:
        nama: Nama mahasiswa yang dicari
        return_all: Jika True, return semua hasil. Jika False, return yang pertama saja
    
    Returns:
        List of dict jika return_all=True, single dict jika return_all=False
    """
    try:
        client = api()
        hasil = client.search_mahasiswa(nama)
        
        if not hasil or len(hasil) == 0:
            return None
        
        if return_all:
            # Return semua hasil
            return [format_mahasiswa_data(mhs) for mhs in hasil]
        else:
            # Return mahasiswa pertama saja
            return format_mahasiswa_data(hasil[0])

    except Exception as e:
        print(f"\n Gagal ambil data melalui pddiktipy: {e}")
        return None

def cari_mahasiswa_by_nim(nim):
    """
    Cari mahasiswa berdasarkan NIM
    
    Args:
        nim: NIM mahasiswa yang dicari
    
    Returns:
        Dictionary berisi data mahasiswa atau None
    """
    try:
        client = api()
        hasil = client.search_mahasiswa(nim)
        
        if not hasil or len(hasil) == 0:
            return None
        
        # Cari yang NIM-nya exact match
        for mhs in hasil:
            if mhs.get("nim", "").lower() == nim.lower():
                return format_mahasiswa_data(mhs)
        
        # Jika tidak ada exact match, return yang pertama
        return format_mahasiswa_data(hasil[0])

    except Exception as e:
        print(f"\n Gagal ambil data melalui pddiktipy: {e}")
        return None
