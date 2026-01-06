from flask import Blueprint, render_template
from repositories.repository_factory import RepositoryFactory

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/my-orders')
def show_my_orders():
    factory = RepositoryFactory()
    repo = factory.get_repository("order")
    data = repo.get_all_orders()
    return render_template('my_orders.html', orders=data)