from flask import Blueprint, flash, redirect, render_template, request, url_for
from models.user import User
from controllers.user import create_user

website = Blueprint("website", __name__, url_prefix="")

@website.route("/")
def index():
    return render_template("website/index.html")

@website.route("/login")
def login():
    return render_template("website/login.html")

@website.route("/signup")
def signup():
    return render_template("website/signup.html")

@website.route("/signup_user", methods=["POST"])
def signup_user():
    try:
        if request.method == "POST":
            user =  User(
                firstname = request.form.get("firstname"),
                lastname = request.form.get("lastname"),
                email = request.form.get("email"),
                password = request.form.get("password"),
                street = request.form.get("street"),
                house_number = request.form.get("house_number"),
                city = request.form.get("city"),
                zip_code = request.form.get("zip_code")
            )
            create_user(user)
        return redirect(url_for("website.login"))
    except Exception as ex:
        return str(ex)