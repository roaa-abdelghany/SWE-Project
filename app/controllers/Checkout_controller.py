from flask import request, render_template, Blueprint
from models.Checkout import Checkout
from repositories.cart_repository import CartRepository

checkout_bp = Blueprint('checkout', __name__, url_prefix='/checkout')

@checkout_bp.route("/<int:user_id>", methods=["GET"])
def show_checkout_page(user_id):
    items = CartRepository.get_by_user(user_id)
    Checkout= Checkout("", "", "", items)
    order_summary = Checkout.order_summary()
    return render_template(
        "checkout.html", items=items, user_id=user_id,subtotal=order_summary["subtotal"],shipping_fee=order_summary["shipping_fee"],total=order_summary["total"])

@checkout_bp.route("/<int:user_id>", methods=["POST"])
def process_checkout(user_id):
    shipping_address = request.form.get("shipping_address")
    phone_number = request.form.get("phone_number")
    payment_method = request.form.get("payment_method")

    items = CartRepository.get_by_user(user_id)

    checkout = Checkout(shipping_address, phone_number, payment_method, items)
    order_summary = checkout.order_summary()

    return render_template("order_confirmation.html",**order_summary )