from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from repositories.repository_factory import RepositoryFactory

favorite_bp = Blueprint('favorite', __name__)

@favorite_bp.route('/favorites')
def favorites():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    repo = RepositoryFactory.get_repository("favorite")
    data = repo.get_all()
    
    cart_repo = RepositoryFactory.get_repository("cart")
    cart_items = cart_repo.get_by_user(session.get('user_id', 1))
    
    return render_template("favorites.html", favorites=data, cart_count=len(cart_items))

@favorite_bp.route('/add_favorite/<product_id>', methods=['POST'])
def add_favorite(product_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    product_repo = RepositoryFactory.get_repository("product")
    all_products = product_repo.get_all()
    
    product = next((p for p in all_products if str(p.id) == str(product_id)), None)
    
    if product:
        favorite_repo = RepositoryFactory.get_repository("favorite")
        product_dict = {
            "product_id": str(product.id),
            "name": product.name,
            "category": product.category,
            "price": str(product.price),
            "stock": str(product.stock),
            "image": product.image,
            "description": getattr(product, 'description', ''),
            "rank": getattr(product, 'rank', 0)
        }
        favorite_repo.add_favorite(product_dict)
        flash("Product added to wishlist!", "success")
    
    return redirect(url_for('favorite.favorites'))

@favorite_bp.route('/remove_favorite/<product_id>')
def remove_favorite(product_id):
    repo = RepositoryFactory.get_repository("favorite")
    repo.remove_favorite(product_id)
    return redirect(url_for('favorite.favorites'))
