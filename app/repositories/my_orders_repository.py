# my_orders_repository.py
from datetime import datetime
from models.my_orders import OrderModel 

class OrderRepository:
    _instance = None

    def __new__(cls):
      
        if cls._instance is None:
            cls._instance = super(OrderRepository, cls).__new__(cls)
            cls._instance._data = [
                {
                    "id": 1024, 
                    "product": "Velvet Matte Lipstick (Initial Order)", 
                    "date": "2023-12-01", 
                    "status": "Delivered", 
                    "price": 25.0
                }
            ]
        return cls._instance

    def get_all_orders(self):
        return self._data

    def add_order(self, product_names, total_price):
 
        new_id = self._data[-1]["id"] + 1 if self._data else 1001
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        new_order_obj = OrderModel(new_id, product_names, current_date, total_price)
        
        self._data.append(new_order_obj.to_dict())
        
        print(f"Order #{new_id} has been added to the repository successfully.")

class RepositoryFactory:
  
    @staticmethod
    def get_repository(repo_type):
        if repo_type == "order":
            return OrderRepository()
        return None