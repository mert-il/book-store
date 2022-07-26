import os
from datetime import datetime
from flask import Blueprint, flash, render_template, request, redirect, session
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
def load_user(user_id: str) -> User:
    return user_logic.get_by_id(user_id)

@website.route("/")
def index():
    session["shopping_card"] = list()
    return render_template("website/index.html")

@website.route("/login")
def login():
    return render_template("website/login.html")

@website.post("/login-user")
def user_login():
    email = request.form.get("email")
    password = request.form.get("password")
    user = user_logic.get(email, password)
    if user != None:
        login_user(user)
        flash(f"Welcome back, {user.firstname} {user.lastname}!", "success")
        return redirect("/")
    else:
        flash(f"Login failed!", "danger")
        return redirect("/login")


@website.route("/logout")
def user_logout():
    logout_user()
    flash("You have been logged out!", "success")
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
    session["shopping_card"].append(book_logic.get_by_id(id))
    return render_template("website/bookview.html", book=book_logic.get_by_id(id))

@website.route("/genres")
def genres():
    return render_template("website/genres.html", genres=genre_logic.get_all())

@website.route("/account")
@login_required
def account():
    return render_template("website/account.html")

@website.route("/order-history")
@login_required
def order_history():
    return render_template("website/order_history.html", orders=order_logic.get_by_user(current_user))

@website.route("change-password")
@login_required
def change_password():
    return render_template("website/change_password.html")

@website.post("user-change-password")
@login_required
def user_change_password():
    user_id = current_user.id 
    old_password = request.form.get("old_password")
    new_password = request.form.get("new_password_1")
    new_password_repeat = request.form.get("new_password_2")
    if new_password == new_password_repeat:
        user_logic.change_password(user_id, old_password, new_password)
        flash("Your password was successfully changed!", "success")
    else:
        flash("An error occurred while changing the password!", "danger")
        return redirect("/change-password")
    return redirect("/account") 


@website.post("/update")
@login_required
def user_update():
    user_id = current_user.id
    new_user_data = User(
        firstname = request.form.get("firstname"),
        lastname = request.form.get("lastname"),
        email = request.form.get("email"),
        street = request.form.get("street"),
        housenumber = request.form.get("housenumber"),
        city = request.form.get("city"),
        zipcode = request.form.get("zipcode")
    )
    user_logic.update(user_id, new_user_data)
    flash("Your Account has been updated!", "success")
    return redirect("/account")

@website.route("/delete")
@login_required
def delete_account():
    return render_template("website/delete.html")

@website.post("/user-delete")
@login_required
def user_delete_account():
    user = current_user
    user_logic.delete(user.id)
    flash("Your account was successfully deleted!", "success")
    mail_message = f"""Hello {user.firstname} {user.lastname},
    your account was successfully deleted!
    """
    send_mail_queued(os.environ.get("MAIL_USERNAME"), user.email, "Bookstore: Delete Account", mail_message)
    redirect("/logout")

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

