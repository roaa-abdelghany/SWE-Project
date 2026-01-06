import csv
import os

CSV_PATH = 'data/favorites.csv'

def get_all_favorites():
    """Reads the CSV and returns a list of dictionaries."""
    if not os.path.exists(CSV_PATH):
        return []
    with open(CSV_PATH, mode='r') as f:
        return list(csv.DictReader(f))

def save_favorites(fav_list):
    """Takes a list of dictionaries and saves it to the CSV."""
    if not fav_list: return
    keys = fav_list[0].keys()
    with open(CSV_PATH, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(fav_list)