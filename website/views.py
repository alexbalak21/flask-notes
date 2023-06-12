from flask import Blueprint

views = Blueprint('views', __name__)

@views.get('/')
def home():
    return "<h1>Home</h1>"