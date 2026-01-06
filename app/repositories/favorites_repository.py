import csv
import os

FAVORITES_FILE = "data/favorites.csv"

class FavoriteRepository:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FavoriteRepository, cls).__new__(cls)
            if not os.path.exists("data"):
                os.makedirs("data")
            if not os.path.exists(FAVORITES_FILE):
                with open(FAVORITES_FILE, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["product_id","name","category","price","stock","rank","description","image"])
        return cls._instance

    def get_all(self):
        favorites = []
        if not os.path.exists(FAVORITES_FILE):
            return favorites
            
        with open(FAVORITES_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                favorites.append(row)
        return favorites

    def add_favorite(self, product):
        favorites = self.get_all()
        if not any(f['product_id'] == str(product['product_id']) for f in favorites):
            with open(FAVORITES_FILE, "a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=product.keys())
                writer.writerow(product)

    def remove_favorite(self, product_id):
        favorites = self.get_all()
        updated_favorites = [f for f in favorites if f['product_id'] != str(product_id)]
        
        with open(FAVORITES_FILE, "w", newline="", encoding="utf-8") as f:
            if updated_favorites:
                writer = csv.DictWriter(f, fieldnames=updated_favorites[0].keys())
                writer.writeheader()
                writer.writerows(updated_favorites)
            else:
                f.write("product_id,name,category,price,stock,rank,description,image\n")
