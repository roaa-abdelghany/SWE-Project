from models.cart import CartItem
from core.file_singleton import FileManager

class CartRepository:
    def __init__(self):
        self.file = FileManager()
        self.path = "data/Cart_items.csv"
        
    def get_all(self):
        rows = self.file.read_csv(self.path)
        return [
            CartItem(
                r["user_id"],
                r["product_id"],
                int(r["quantity"])
            )
            for r in rows
        ]   
        
    @staticmethod
    def get_by_user(user_id):
        repo = CartRepository()
        all_items = repo.get_all()
        return [item for item in all_items if item.user_id == user_id]
    
    def get_item(self, user_id, product_id):
        items = self.get_by_user(user_id)
        for item in items:
            if item.product_id == product_id:
                return item
        return None
    
    def update_quantity(self, cart_items):
        rows = []
        for item in cart_items:
            rows.append({
                "user_id": item.user_id,
                "product_id": item.product_id,
                "quantity": item.quantity,
            })   
        self.file.write_csv(self.path, rows)