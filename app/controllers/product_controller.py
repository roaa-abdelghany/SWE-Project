from flask import Blueprint, render_template, redirect, url_for, session
from repositories.product_repository import ProductRepository

product_bp = Blueprint("product", __name__, url_prefix="/product")
repo = ProductRepository()

@product_bp.route("/product/<int:id>")
def product_details(id):
    product = repo.get_by_id(id)
    if not product:
        return "Product not found", 404
    
    return render_template("product_details.html", product=product)
