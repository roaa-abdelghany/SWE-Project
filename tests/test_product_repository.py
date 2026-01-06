from app.repositories.product_repository import ProductRepository

def test_get_products():
    repo = ProductRepository()
    products = repo.get_all()
    assert len(products) >= 0