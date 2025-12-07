from flask import request,render_template
from models.Checkout import Checkout
from repositories.cart_repository import cartrepository

class CheckoutController:
    @staticmethod
    def show_checkout_page(user_id):
        items=cartrepository.get_items_by_user_id(user_id)
        return render_template("checkout.html", items=items)
    @staticmethod
    def process_checkout(user_id):
        shipping_address = request.form("shipping_address")
        phone_number = request.form("phone_number")
        payment_method = request.form("payment_method")
        items = cartrepository.get_items_by_user_id(user_id)
        checkout = Checkout(shipping_address, phone_number, payment_method, items)
        order_summary = checkout.order_summary()
        return render_template("order_confirmation.html", order_summary=order_summary)