import csv
import os

PRODUCTS_FILE = "data/products.csv"
ORDERS_FILE = "data/orders.csv"

class AdminDetailsRepository:
    def __init__(self):
        self.product_fields = ["id", "name", "category", "price", "stock", "image"]
        self.order_fields = ["id", "user_id", "customer_name", "date", "total", "status"]

    def get_all_products(self):
        products = []
        if not os.path.exists(PRODUCTS_FILE): return products
        with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
            return list(csv.DictReader(f))

    def add_product(self, data):
        products = self.get_all_products()
        products.append(data)
        self._write_all_products(products)

    def delete_product(self, product_id):
        products = self.get_all_products()
        updated = [p for p in products if str(p['id']) != str(product_id)]
        self._write_all_products(updated)

    def _write_all_products(self, products):
        with open(PRODUCTS_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.product_fields)
            writer.writeheader()
            for p in products:
                filtered_dict = {k: p.get(k, "") for k in self.product_fields}
                writer.writerow(filtered_dict)

    def get_all_orders(self):
        if not os.path.exists(ORDERS_FILE): return []
        with open(ORDERS_FILE, "r", encoding="utf-8") as f:
            return list(csv.DictReader(f))

    def save_new_order(self, order_data):
        file_exists = os.path.isfile(ORDERS_FILE)
        with open(ORDERS_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.order_fields)
            if not file_exists or os.path.getsize(ORDERS_FILE) == 0:
                writer.writeheader()
            writer.writerow(order_data)