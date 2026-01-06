from flask import Flask, render_template, session, redirect, url_for

from repositories.product_repository import ProductRepository
from controllers.auth_controller import auth_bp
from controllers.product_controller import product_bp
from controllers.cart_controller import cart_bp
from controllers.Checkout_controller import checkout_bp
from controllers.admin_controller import admin_bp as admin_auth_bp
from controllers.admin_product_controller import admin_bp as admin_panel_bp
from controllers.favorites_controller import favorite_bp
from controllers.my_orders_controller import orders_bp 
from repositories.repository_factory import RepositoryFactory

def inject_cart_count():
    user_id = session.get('user_id', 1)
    try:
        cart_repo = RepositoryFactory.get_repository("cart")
        cart_items = cart_repo.get_by_user(user_id)
        return dict(cart_count=len(cart_items))
    except:
        return dict(cart_count=0)

app = Flask(__name__)
app.secret_key = "secret_key_glowing_cosmetics" 

product_repo = ProductRepository()

app.register_blueprint(auth_bp)
app.register_blueprint(product_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(checkout_bp)
app.register_blueprint(admin_auth_bp)
app.register_blueprint(admin_panel_bp)
app.register_blueprint(favorite_bp)
app.register_blueprint(orders_bp) 


@app.route("/")
def index():
    return render_template("landing.html")

@app.route("/home")
def home():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    all_products = product_repo.get_all() 
    return render_template("home.html", products=all_products)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)