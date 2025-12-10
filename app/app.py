from flask import Flask, render_template
#from controllers.cart_controller import cart_bp
#from controllers.product_controller import product_bp
from controllers.Checkout_controller import checkout_bp

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

#app.register_blueprint(product_bp)      
#app.register_blueprint(cart_bp)        
app.register_blueprint(checkout_bp)     

if __name__ == "__main__":
    app.run(debug=True)