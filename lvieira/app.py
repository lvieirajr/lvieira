# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from flask import Flask, render_template
from flask.ext.login import LoginManager
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
from mongoengine import connect


__all__ = [
    'app',
    'db',
    'login_manager'
]


# Creating the Flask object and settings the configurations
app = Flask(__name__)
app.config.from_object('lvieira.settings')

# Adding the 'home' url rule
app.add_url_rule(
    '/',
    endpoint='home',
    view_func=lambda: render_template('index.html'),
    methods=['GET']
)

# Adding the 'about' url rule
app.add_url_rule(
    '/about',
    endpoint='about',
    view_func=lambda: render_template('about.html'),
    methods=['GET']
)

# Setting up the login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'pai.login'

# Setting up database
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)

# Creating the connection to the database
connect(app.config.get('MONGO_DBNAME'), host=app.config.get('MONGO_URI'))







