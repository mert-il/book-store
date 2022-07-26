from flask import Blueprint, render_template, request, redirect
from logic.admin import AdminLogic
from logic.book import BookLogic
from models.admin import Admin
from services.auth import login_manager
from flask_login import current_user, login_required, login_user, logout_user

admin = Blueprint("admin", __name__, url_prefix="/admin")

admin_logic = AdminLogic()
book_logic = BookLogic()

#@login_manager.use_loader
#def load_admin(admin_id: str) -> Admin:
#    return admin_logic.get_by_id(admin_id)

@admin.route("/")
def index():
    return render_template("admin/index.html")

@admin.route("login")
def login():
    return render_template("admin/login.html")

@admin.post("login-admin")
def admin_login():
    email = request.form.get("email")
    password = request.form.get("password")
    admin = admin_logic.get(email, password)
    login_user(admin)
    return redirect("/")

@admin.route("books")
def books():
    return render_template("admin/books.html", books=book_logic.get_all())

@admin.route("book-add")
def book_add():
    return render_template("admin/add_book.html")

