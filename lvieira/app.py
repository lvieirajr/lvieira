# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine

from .blueprints import pai_blueprint

__all__ = [
    'app',
    'db'
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

# Registering blueprints
app.register_blueprint(pai_blueprint)

# Creating the database
db = MongoEngine(app)
