import json
import csv
import os
from datetime import datetime

def export_to_json(data, filename=None):
    """Export data ke JSON file"""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"export_studentsnipe_{timestamp}.json"
    
    os.makedirs("exports", exist_ok=True)
    filepath = os.path.join("exports", filename)
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return filepath
    except Exception as e:
        return None

def export_to_csv(data, filename=None):
    """Export data ke CSV file"""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"export_studentsnipe_{timestamp}.csv"
    
    os.makedirs("exports", exist_ok=True)
    filepath = os.path.join("exports", filename)
    
    try:
        # Jika data adalah list of dict
        if isinstance(data, list) and len(data) > 0:
            keys = data[0].keys()
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)
        # Jika data adalah single dict
        elif isinstance(data, dict):
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=data.keys())
                writer.writeheader()
                writer.writerow(data)
        
        return filepath
    except Exception as e:
        return None

def export_to_txt(data, filename=None):
    """Export data ke TXT file"""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"export_studentsnipe_{timestamp}.txt"
    
    os.makedirs("exports", exist_ok=True)
    filepath = os.path.join("exports", filename)
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("StudentSnipe - Export Data\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 60 + "\n\n")
            
            if isinstance(data, list):
                for idx, item in enumerate(data, 1):
                    f.write(f"--- Record {idx} ---\n")
                    for key, value in item.items():
                        f.write(f"{key:<20}: {value}\n")
                    f.write("\n")
            elif isinstance(data, dict):
                for key, value in data.items():
                    f.write(f"{key:<20}: {value}\n")
        
        return filepath
    except Exception as e:
        return None
