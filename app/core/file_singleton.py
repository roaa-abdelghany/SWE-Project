import csv
import threading

class FileManager:

    _instance = None
    _lock = threading.Lock()

    def _new_(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls.instance = super(FileManager, cls).new_(cls)
        return cls._instance

    def read_csv(self, file_path):
        rows = []
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    rows.append(row)
        except FileNotFoundError:
            print(f"Warning: {file_path} not found. Returning empty list.")
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
        return rows

    def write_csv(self, file_path, rows, fieldnames=None):
 
        if not fieldnames and rows:
             fieldnames = list(rows[0].keys())
        
        if not fieldnames:
             print(f"No headers or data to write to {file_path}. Skipping.")
             return
        
        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                writer.writeheader() 
                
                if rows:
                    writer.writerows(rows)
                    
        except Exception as e:
            print(f"Error writing to {file_path}: {e}")