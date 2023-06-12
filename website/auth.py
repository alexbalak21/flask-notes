from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "LogIn"

@auth.route('/logout')
def logout():
    return "LogOut"

@auth.route('/sign-up')
def sign_up():
    return "Sign-up"