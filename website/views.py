from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.get('/')
def home():
    return "<h1>Home</h1>"


@views.get('/passgen')
def passgen():
    return render_template("password.html")
