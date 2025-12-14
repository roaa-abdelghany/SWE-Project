from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from repositories.user_repository import UserRepository
from models.user import User 

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        fullname = request.form.get("fullname")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm_password")

        if password != confirm:
            flash("Passwords do not match!", "error")
            return redirect(url_for("auth.register"))

        user = User(fullname, email, password)
        UserRepository.add_user(user)

        flash("Account created successfully!", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = UserRepository.find_user_by_email_and_password(email, password)

        if user:
            session['user_id'] = user.email
            session['fullname'] = user.fullname
            flash(f"Welcome, {user.fullname}!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid email or password!", "error")
            return redirect(url_for("auth.login"))

    return render_template("login.html")