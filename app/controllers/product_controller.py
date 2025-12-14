from flask import Blueprint, redirect, render_template, session, url_for    
from repositories.product_repository import ProductRepository
from repositories.cart_repository import CartRepository

product_bp = Blueprint("product", __name__, url_prefix="/product")
repo = ProductRepository()

@product_bp.route("/<int:id>")
def product_details(id):
    product = repo.get_by_id(id)
    if not product:
        return "Product not found", 404
    
    if 'user_id' not in session:
            return redirect(url_for('auth.login'))
    user_id = session['user_id'] 
    cart_repo = CartRepository()
    cart_items = cart_repo.get_by_user(user_id)
    cart_count = len(cart_items)
    
    return render_template("product_details.html", product=product, cart_count=cart_count)