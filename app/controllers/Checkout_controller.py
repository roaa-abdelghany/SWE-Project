from flask import request, render_template, Blueprint
from models.Checkout import Checkout
from repositories.cart_repository import CartRepository

checkout_bp = Blueprint('checkout', __name__, url_prefix='/checkout')

@checkout_bp.route("/<int:user_id>", methods=["GET"])
def show_checkout_page(user_id):
    items = CartRepository.get_by_user(user_id)
    subtotal = sum(item.price * item.quantity for item in items)
    shipping_fee = 0 if (subtotal >= 100 or subtotal==0) else 50
    total = subtotal + shipping_fee
    return render_template(
        "checkout.html",
        items=items,
        user_id=user_id,
        subtotal=subtotal,
        shipping_fee=shipping_fee,
        total=total
    )

@checkout_bp.route("/<int:user_id>", methods=["POST"])
def process_checkout(user_id):
    shipping_address = request.form.get("shipping_address")
    phone_number = request.form.get("phone_number")
    payment_method = request.form.get("payment_method")

    items = CartRepository.get_by_user(user_id)

    checkout = Checkout(shipping_address, phone_number, payment_method, items)
    order_summary = checkout.order_summary()

    return render_template("order_confirmation.html",**order_summary )