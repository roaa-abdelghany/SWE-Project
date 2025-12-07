from flask import Flask
from controllers.sign in_controller import sign in_bp

app = Flask(_name_)
app.register_blueprint(sign in_bp) 

if _name_ == "_main_":
    app.run(debug=True)
    
    