# models/my_orders.py

class OrderModel:
    def __init__(self, order_id, product_names, date, total_price, status="Processing"):
    
        self.id = order_id
        self.product_names = product_names
        self.date = date
        self.total_price = total_price
        self.status = status

    def to_dict(self):
   
        return {
            "id": self.id,
            "product": self.product_names,
            "date": self.date,
            "price": self.total_price,
            "status": self.status
        }