from flask import Blueprint, render_template, request, redirect
from logic.user import UserLogic
from logic.book import BookLogic
from flask_login import current_user, login_required, login_user, logout_user
from services.auth import login_manager
from models.user import User

website = Blueprint("website", __name__, url_prefix="")

user_logic = UserLogic()
book_logic = BookLogic()

@login_manager.user_loader
def load_user(user_id):
    return user_logic.get_by_id(user_id)

@website.route("/")
def index():
    return render_template("website/index.html")

@website.route("/login")
def login():
    return render_template("website/login.html")

@website.post("/login-user")
def user_login():
    email = request.form.get("email")
    password = request.form.get("password")
    user = user_logic.get(email, password)
    login_user(user.get_id())
    return redirect("/login-test")

@website.route("/signup")
def signup():
    return render_template("website/signup.html")

@website.post("signup-user")
def user_signup():
    user = User(
        firstname = request.form.get("firstname"),
        lastname = request.form.get("lastname"),
        email = request.form.get("email"),
        password = request.form.get("password"),
        street = request.form.get("street"),
        housenumber = request.form.get("housenumber"),
        city = request.form.get("city"),
        zipcode = request.form.get("zipcode")
    )
    user_logic.save(user)
    return redirect("/")

@website.route("/books")
def books():
    return render_template("website.books.html", books=book_logic.get_all())

@website.get("book-view")
def book_view():
    id = request.args.get("id") 
    return render_template("website/bookview.html", book=book_logic.get_by_id(id))
