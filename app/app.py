from flask import Flask, render_template, session, redirect, url_for

from controllers.auth_controller import auth_bp
from controllers.product_controller import product_bp
from controllers.cart_controller import cart_bp
from controllers.Checkout_controller import checkout_bp

app = Flask(__name__)
app.secret_key = "secret_key_glowing_cosmetics" 

app.register_blueprint(auth_bp)
app.register_blueprint(product_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(checkout_bp)

@app.route("/")
def home():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)