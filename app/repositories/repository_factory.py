from repositories.user_repository import UserRepository
from repositories.product_repository import ProductRepository
from repositories.cart_repository import CartRepository


class RepositoryFactory:
    @staticmethod
    def get_repository(entity_type):
        if entity_type == "user":
            return UserRepository()
        elif entity_type == "product":
             return ProductRepository()
        elif entity_type == "cart":
             return CartRepository()
        else:
            raise ValueError("Unknown repository type")