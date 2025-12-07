from models.product import Product
from core.singleton import FileManager


class ProductRepository:
    def __init__(self):
        self.file = FileManager()

    def get_all(self):
        rows = self.file.read_csv("data/Products.csv")
        products = []

        for r in rows:
            product = Product(
                int(r["id"]),
                r["name"],
                r["category"],
                float(r["price"]),
                int(r["stock"]),
                float(r["rank"]),
                r["description"],
                r["image"],
            )
            products.append(product)
        return products

    def get_by_id(self, id):
        all_products = self.get_all()
        for product in all_products:
            if product.id == id:
                return product
        return None
