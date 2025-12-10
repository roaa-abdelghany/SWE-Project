from flask import Flask
from controllers.product_controller import product_bp
from controllers.cart_controller import cart_bp
from controllers.Checkout_controller import checkout_bp


app = Flask(__name__)
app.register_blueprint(checkout_bp) 

#app = Flask(__name__)
#app.register_blueprint(cart_bp) 

#app = Flask(__name__)
#app.register_blueprint(product_bp) 

if __name__ == "__main__":
    app.run(debug=True)