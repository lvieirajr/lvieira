# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from flask import Flask, render_template

from .blueprints import pai_blueprint

__all__ = [
    'create_app',
]


def create_app():
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

    return app
