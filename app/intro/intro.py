from flask import render_template
# intro_bp from init in this folder
from . import intro_bp


@intro_bp.route("/")
def home():
    return render_template("index.html")


@intro_bp.route("/about")
def about():
    return render_template("about.html")
