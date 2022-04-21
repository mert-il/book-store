from flask import Blueprint, render_template
from models.publisher import Publisher

website = Blueprint("website", __name__, url_prefix="")

@website.route("/")
def index():
    pub = Publisher(name="Test")
    pub.save()
    return render_template("website/index.html")