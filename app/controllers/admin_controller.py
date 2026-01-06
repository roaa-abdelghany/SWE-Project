from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from repositories.admin_repository import AdminRepository

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        admin = AdminRepository.find_admin(email, password)

        if admin:
            session['admin_logged_in'] = True
            flash("Welcome Admin!", "success")
            return redirect(url_for("admin_panel.admin_dashboard"))
        else:
            flash("Invalid admin credentials", "error")

    return render_template("admin_login.html")