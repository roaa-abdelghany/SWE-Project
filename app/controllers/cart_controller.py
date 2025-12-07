from flask import Blueprint, render_template
import csv
import os

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")

def read_cart():
    cart_items = []
    cart_total = 0.0
    cart_file = os.path.join("data", "Cart_items.csv")
    
    if os.path.exists(cart_file):
        with open(cart_file, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                total = float(row["price"]) * int(row["quantity"])
                cart_total += total
                cart_items.append({
                    "product_id": row["product_id"],
                    "name": row.get("name", "Product"),
                    "category": row.get("category", ""),
                    "description": row.get("description", ""),
                    "price": float(row["price"]),
                    "quantity": int(row["quantity"]),
                    "total": total
                })
    return cart_items, cart_total

@cart_bp.route("/")
def cart_page():
    cart_items, cart_total = read_cart()
    subtotal = cart_total
    total = round(subtotal)
    return render_template("cart.html",
                           cart_items=cart_items,
                           subtotal=subtotal,
                           total=total)