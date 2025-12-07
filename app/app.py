from flask import Flask
# from controllers.cart_controller import cart_bp
from controllers.auth_controller import auth_bp

app = Flask(__name__)
# app.register_blueprint(cart_bp) 
app.register_blueprint(auth_bp) 


if __name__ == "__main__":
    app.run(debug=True)
    
    
    