# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from flask import Flask, render_template
from os import path

from .blueprints import pai_blueprint

__all__ = [
    'create_app',
]


def create_app(mode):
    # Selecting correct instance (Development or Production)
    instance_path = path.join(
        path.abspath(path.dirname(__file__)), '%s_instance' % mode
    )

    # Creating the Flask object for the given instance
    app = Flask(
        'lvieira',
        instance_path=instance_path,
        instance_relative_config=True
    )

    # Setting the app configurations
    app.config.from_object('lvieira.settings')
    app.config.from_pyfile('config.cfg')

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
