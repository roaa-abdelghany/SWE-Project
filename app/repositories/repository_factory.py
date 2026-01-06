class RepositoryFactory:
    @staticmethod
    def get_repository(entity_type):
        if entity_type == "user":
            from repositories.user_repository import UserRepository
            return UserRepository()
        
        elif entity_type == "product":
            from repositories.product_repository import ProductRepository
            return ProductRepository()
        
        elif entity_type == "cart":
            from repositories.cart_repository import CartRepository
            return CartRepository()
             
        elif entity_type == "favorite":
            from repositories.favorites_repository import FavoriteRepository
            return FavoriteRepository()
        elif entity_type == "order":
            from repositories.my_orders_repository import OrderRepository
            return OrderRepository()
             
        else:
            raise ValueError("Unknown repository type")