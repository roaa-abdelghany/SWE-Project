from models.cart import CartItem
from core.file_singleton import FileManager
from typing import List

CART_HEADERS = ["user_id", "product_id", "quantity"]

class CartRepository:
    def __init__(self):
        self.file = FileManager()
        self.path = "data/Cart_items.csv"
        
    def _read_all_items(self) -> List[CartItem]:
        rows = self.file.read_csv(self.path)
        return [
            CartItem(
                user_id=r["user_id"],
                product_id=r["product_id"],
                quantity=int(r["quantity"])
            )
            for r in rows
        ] 

    def _write_all_items(self, items: List[CartItem]):
        rows = [{
            "user_id": item.user_id,
            "product_id": item.product_id,
            "quantity": item.quantity
        } for item in items]

        self.file.write_csv(self.path, rows, fieldnames=CART_HEADERS)
        
    @staticmethod
    def get_by_user(user_id):
        repo = CartRepository()
        all_items = repo._read_all_items()
        return [item for item in all_items if str(item.user_id) == str(user_id)]
    
    def get_item(self, user_id: str, product_id: str) -> CartItem or None:
        items = self.get_by_user(user_id)
        for item in items:
            if item.product_id == product_id:
                return item
        return None
    
    def add_item(self, user_id: str, product_id: str, quantity: int):
        all_items = self._read_all_items()
        
        new_item = CartItem(
            user_id=user_id,
            product_id=product_id,
            quantity=quantity
        )
        all_items.append(new_item)
        self._write_all_items(all_items)
    
    def update_cart(self, user_id: str, updated_item: CartItem):
        all_items = self._read_all_items()
        found = False
        
        for i, item in enumerate(all_items):
            if item.user_id == user_id and item.product_id == updated_item.product_id:
                all_items[i].quantity = updated_item.quantity 
                found = True
                break
        
        final_items = [item for item in all_items if item.quantity > 0]
        self._write_all_items(final_items)
        return found
        
    def delete_item(self, user_id: str, product_id: str):
        all_items = self._read_all_items()
        
        final_items = [
            item for item in all_items 
            if not (item.user_id == user_id and item.product_id == product_id)
        ]
        
        self._write_all_items(final_items)
