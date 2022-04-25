from flask import Blueprint, render_template
website = Blueprint("website", __name__, url_prefix="")

@website.route("/")
def index():
    return render_template("website/index.html")