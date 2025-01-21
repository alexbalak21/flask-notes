
from flask import Blueprint, jsonify, render_template
from model import test_conn, test_create
routes = Blueprint('routes', __name__)


@routes.get('/')
def home():
    return "<h1>Home</h1>"


@routes.get('/db')
def db_conn():

    return test_conn()


@routes.get('/test')
def test():
    return "Test"


@routes.get('/api')
def rest_api():
    return jsonify({'Hello': 'World'})


@routes.get('/down')
def down():
    return render_template('down.html')


@routes.get('/create')
def create_test_note():
    return test_create()


@routes.get('/passgen')
def pass_gen():
    return render_template("passwrd.html")
