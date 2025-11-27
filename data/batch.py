import csv
import time
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from data.api_client import cari_mahasiswa, cari_mahasiswa_by_nim

def read_batch_file(filepath):
    """Baca file batch (TXT atau CSV)"""
    queries = []
    
    try:
        # Coba baca sebagai CSV
        if filepath.endswith('.csv'):
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row and row[0].strip():
                        queries.append(row[0].strip())
        else:
            # Baca sebagai TXT (satu nama per baris)
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        queries.append(line)
        
        return queries
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def process_batch(queries, search_type="nama"):
    """Process batch queries dengan progress bar"""
    results = []
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        
        task = progress.add_task("[cyan]Processing batch...", total=len(queries))
        
        for query in queries:
            try:
                if search_type == "nim":
                    data = cari_mahasiswa_by_nim(query)
                else:
                    data = cari_mahasiswa(query, return_all=True)
                
                if data:
                    if isinstance(data, list):
                        results.extend(data)
                    else:
                        results.append(data)
                
                time.sleep(0.5)  # Rate limiting
            except Exception as e:
                print(f"Error processing '{query}': {e}")
            
            progress.update(task, advance=1)
    
    return results
