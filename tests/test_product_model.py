from app.models.product import Product

def test_product_creation():
    p = Product(
        1,
        "Perfume",
        "Fragrance",
        200.0,
        5,
        4.5,
        "Nice",
        "img.jpg"
    )

    assert p.name == "Perfume"
    assert p.stock == 5