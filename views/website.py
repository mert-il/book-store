from flask import Blueprint, redirect, render_template, request, url_for
from models.book import Book
from models.user import User
from logic.user import UserLogic
from logic.book import BookLogic
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

website = Blueprint("website", __name__, url_prefix="")

@website.route("/")
def index():
    return render_template("website/index.html")

@website.route("/account")
def account():
    return redirect(url_for("website.login"))

@website.route("/login")
def login():
    return render_template("website/login.html")

@website.route("/login_user", methods=["POST"])
def login_user():
    try:
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
        user = UserLogic().get(email, password)
        access_token = create_access_token(identity=user.id)
        return redirect(url_for("website.index"))
    except Exception as e:
        return str(e)

@website.route("/signup")
def signup():
    return render_template("website/signup.html")

@website.route("/signup_user", methods=["POST"])
def signup_user():
    try:
        if request.method == "POST":
            user = User(
                firstname = request.form.get("firstname"),
                lastname = request.form.get("lastname"),
                email = request.form.get("email"),
                password = request.form.get("password"),
                street = request.form.get("street"),
                housenumber = request.form.get("house_number"),
                city = request.form.get("city"),
                zipcode = request.form.get("zip_code")
            )
            UserLogic().create(user)
        return redirect(url_for("website.login"))
    except Exception as e:
        return str(e)

@website.route("/books")
def books():
    return render_template("website/books.html", books=BookLogic().get_all())

@website.route("/book")
def book():
    try:
        id = request.args.get("id")
        return render_template("website/bookview.html", book=BookLogic().get(id))
    except Exception as e:
        return str(e)