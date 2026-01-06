from flask import Blueprint, render_template, request, redirect, session, url_for
from repositories.admin_product_repository import AdminDetailsRepository

admin_bp = Blueprint("admin_panel", __name__, url_prefix="/admin-dashboard")

@admin_bp.route("/")
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin.admin_login'))
    
    repo = AdminDetailsRepository()
    products = repo.get_all_products()
    orders = repo.get_all_orders()
    return render_template("admin_products.html", products=products, orders=orders)

@admin_bp.route("/add_product", methods=["POST"])
def add_product():
    repo = AdminDetailsRepository()
    products = repo.get_all_products()
    new_id = str(len(products) + 1)
    
    new_product = {
        "id": new_id,
        "name": request.form.get("name"),
        "category": request.form.get("category"),
        "price": request.form.get("price"),
        "stock": request.form.get("stock"),
        "image": "default.png"
    }
    repo.add_product(new_product)
    return redirect(url_for("admin_panel.admin_dashboard"))

@admin_bp.route("/delete/<product_id>")
def delete_product(product_id):
    repo = AdminDetailsRepository()
    repo.delete_product(product_id)
    return redirect(url_for("admin_panel.admin_dashboard"))