from flaskext.mysql import MySQL
from app import app

mysql = MySQL()
mysql.init_app(app)


def prodDB():
    app.config['MYSQL_DATABASE_HOST'] = 'mysql-alex.alwaysdata.net'
    app.config['MYSQL_DATABASE_USER'] = 'alex'
    app.config['MYSQL_DATABASE_PASSWORD'] = '6hxCKt6yeo6Jb?mYK4tTxd$p@tnh7PAjxJEGmT@E'
    app.config['MYSQL_DATABASE_DB'] = 'alex_db'


def devDB():
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'test'


def test_conn():
    try:
        connect = mysql.connect()
        connect.cursor()
        return 'Success'
    except:
        return 'Failed'


def test_create():
    try:
        connect = mysql.connect()
        cursor = connect.cursor()
        qry = """INSERT INTO notes (content) VALUES (%s);"""
        note = 'Note Production Working'
        cursor.execute(qry, (note,))
        connect.commit()
        connect.close()
        return 'Added to db'
    except:
        return 'Failed to add to db.'
