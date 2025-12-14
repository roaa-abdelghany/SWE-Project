from flask import redirect, request, render_template, Blueprint, session, url_for
from models.Checkout import Checkout
from repositories.cart_repository import CartRepository
from repositories.product_repository import ProductRepository
import csv
import os

checkout_bp = Blueprint('checkout', __name__, url_prefix='/checkout')
PRODUCTS_FILE = "data/Products.csv"

def get_products_dict():
    products = {}
    if os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products[row["product_id"]] = row
    return products

@checkout_bp.route("/", methods=["GET"])
def show_checkout_page():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user_id = session['user_id'] 
    
    cart_repo = CartRepository()
    items = cart_repo.get_by_user(user_id)
    
    products = get_products_dict()
    calculated_subtotal = 0.0
    for item in items:
        product = products.get(item.product_id) 
        if product:
            price = float(product.get("price", 0.0))
            quantity = int(item.quantity)
            calculated_subtotal += price * quantity
    
    checkout= Checkout(None, None, None, calculated_subtotal)
    order_summary = checkout.order_summary()
    
    return render_template(
        "checkout.html", items=items, user_id=user_id,**order_summary)

@checkout_bp.route("/process", methods=["POST"])
def process_checkout():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user_id = session['user_id'] 
    shipping_address = request.form.get("shipping_address")
    phone_number = request.form.get("phone_number")
    payment_method = request.form.get("payment_method")
    
    cart_repo = CartRepository()
    items = cart_repo.get_by_user(user_id)
    products = get_products_dict()
    calculated_subtotal = 0.0
    for item in items:
        product = products.get(item.product_id)
        if product:
            price = float(product.get("price", 0.0))
            quantity = int(item.quantity)
            calculated_subtotal += price * quantity
          
    checkout = Checkout(shipping_address, phone_number, payment_method, calculated_subtotal)
    order_summary = checkout.order_summary()

    return render_template("order_confirmation.html", **order_summary)