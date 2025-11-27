import json
import os
import time
from datetime import datetime, timedelta

CACHE_FILE = "data/.cache.json"
HISTORY_FILE = "data/.history.json"
CACHE_EXPIRY_HOURS = 24

def load_cache():
    """Load cache dari file"""
    if not os.path.exists(CACHE_FILE):
        return {}
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def save_cache(cache_data):
    """Simpan cache ke file"""
    try:
        os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(cache_data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Warning: Gagal menyimpan cache: {e}")

def get_cached_result(query, search_type="nama"):
    """Ambil hasil dari cache jika masih valid"""
    cache = load_cache()
    cache_key = f"{search_type}:{query.lower()}"
    
    if cache_key in cache:
        cached_item = cache[cache_key]
        cached_time = datetime.fromisoformat(cached_item['timestamp'])
        
        if datetime.now() - cached_time < timedelta(hours=CACHE_EXPIRY_HOURS):
            return cached_item['data']
    
    return None

def save_to_cache(query, search_type, data):
    """Simpan hasil pencarian ke cache"""
    cache = load_cache()
    cache_key = f"{search_type}:{query.lower()}"
    
    cache[cache_key] = {
        'timestamp': datetime.now().isoformat(),
        'data': data
    }
    
    save_cache(cache)

def add_to_history(query, search_type, result_count):
    """Tambahkan pencarian ke history"""
    history = load_history()
    
    history.insert(0, {
        'query': query,
        'search_type': search_type,
        'result_count': result_count,
        'timestamp': datetime.now().isoformat()
    })
    
    # Simpan maksimal 50 history terakhir
    history = history[:50]
    
    try:
        os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Warning: Gagal menyimpan history: {e}")

def load_history():
    """Load history dari file"""
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def clear_cache():
    """Hapus semua cache"""
    if os.path.exists(CACHE_FILE):
        os.remove(CACHE_FILE)
    return True
