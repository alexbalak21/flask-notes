from flask import Flask
app = Flask(__name__)
from routes import routes  # noqa


try:
    app.config.from_envvar('APPLICATION_SETTINGS')
except:
    pass

app.register_blueprint(routes, url_prefix='/')
