import os
from datetime import datetime
import re
from flask import Blueprint, render_template, request, redirect
from logic.order import OrderLogic
from logic.user import UserLogic
from logic.book import BookLogic
from logic.genre import GenreLogic
from flask_login import current_user, login_required, login_user, logout_user
from models.order import Order
from services.auth import login_manager
from models.user import User
from services.mail import send_mail_queued

website = Blueprint("website", __name__, url_prefix="")

user_logic = UserLogic()
book_logic = BookLogic()
genre_logic = GenreLogic()
order_logic = OrderLogic()

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
    login_user(user)
    return redirect("/")

@website.route("logout")
def user_logout():
    logout_user()
    return redirect("/")

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

@website.route("/account")
def account():
    return "your account settings"

@website.get("/books")
def books():
    genre_name = request.args.get("genre")
    if genre_name != None:
        genre = genre_logic.get(genre_name)
        return render_template("website/books.html", books=book_logic.get_by_genre(genre))
    else:
        return render_template("website/books.html", books=book_logic.get_all())

@website.get("/book")
def book_view():
    id = request.args.get("id") 
    return render_template("website/bookview.html", book=book_logic.get_by_id(id))

@website.route("/genres")
def genres():
    return render_template("website/genres.html", genres=genre_logic.get_all())

@website.get("/pay")
@login_required
def pay():
    book_id = request.args.get("id")
    book = book_logic.get_by_id(book_id)
    user = current_user
    order = Order(
        user=user,
        book=book,
        date=datetime.now()
    )
    order_logic.save(order)
    mail_message = f"""Ordernumber: {order.id}
    Article: {book.title} - {book.author.name}
    Price: {book.price} €
    """
    send_mail_queued(os.environ.get("MAIL_USERNAME"), user.email, "Bookstore: Your new Order", mail_message)
    return f"u ordered {book.title} for {book.price} €"

