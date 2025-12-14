from flask import Blueprint, render_template, request, redirect, session, url_for
from repositories.cart_repository import CartRepository
from models.cart import CartItem 
import csv
import os

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")

PRODUCTS_FILE = "data/Products.csv"

def get_products_dict():
    products = {}
    if os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products[row["product_id"]] = row
    return products


def get_cart_count(user_id="1"):
    repo = CartRepository()
    items = repo.get_by_user(user_id)
    return sum(item.quantity for item in items)


@cart_bp.route("/add", methods=["POST"])
def add_to_cart():
    try:
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        user_id = session['user_id']   
             
        product_id = request.form.get("product_id")
        quantity = int(request.form.get("quantity", 1))
    except:
        return redirect(request.referrer or url_for("home"))

    if not user_id or not product_id or quantity <= 0:
        return redirect(request.referrer or url_for("home"))

    repo = CartRepository()
    item = repo.get_item(user_id, product_id)

    if item:
        item.quantity += quantity
        repo.update_cart(user_id, item)
    else:
        repo.add_item(user_id, product_id, quantity)

    return redirect(request.referrer or url_for("home"))



@cart_bp.route("/", methods=["GET", "POST"])
def cart_page():
    if 'user_id' not in session:
            return redirect(url_for('auth.login'))
    user_id = session['user_id'] 

    repo = CartRepository()
    products = get_products_dict()

    if request.method == "POST":
        action = request.form.get("action")
        product_id = request.form.get("product_id")

        item = repo.get_item(user_id, product_id)
        if not item:
            return redirect(url_for("cart.cart_page", user_id=user_id))

        if action == "increase":
            item.quantity += 1
            repo.update_cart(user_id, item)

        elif action == "decrease":
            if item.quantity > 1:
                item.quantity -= 1
                repo.update_cart(user_id, item)

        elif action == "delete":
            repo.delete_item(user_id, product_id)

        return redirect(url_for("cart.cart_page", user_id=user_id))

    items = repo.get_by_user(user_id)
    cart_items = []
    subtotal = 0.0
    total_quantity = 0

    for item in items:
        product = products.get(item.product_id)

        if not product:
            continue  

        try:
            price_float = float(product.get("price", 0.0))
            quantity_int = int(item.quantity)
            stock_int = int(product.get("stock", 999))

            item_total = price_float * quantity_int
            subtotal += item_total
            total_quantity += quantity_int

        except:
            continue

        cart_items.append({
            "product_id": item.product_id,
            "name": product["name"],
            "price": price_float,
            "image": product["image"],
            "description": product["description"],
            "quantity": quantity_int,
            "stock": stock_int,
            "item_total": item_total 
        })

    return render_template(
        "cart.html",
        cart_items=cart_items,
        subtotal=subtotal,
        total_quantity=total_quantity,
        cart_count=get_cart_count(user_id),
        total_amount=subtotal
    )
