# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from flask import Flask, render_template
from os import path

__all__ = [
    'create_app',
]


def create_app(mode):
    instance_path = path.join(
        path.abspath(path.dirname(__file__)), '%s_instance' % mode
    )

    app = Flask(
        'lvieira',
        instance_path=instance_path,
        instance_relative_config=True
    )

    app.config.from_object('lvieira.settings')
    app.config.from_pyfile('config.cfg')

    app.add_url_rule(
        '/',
        endpoint='home',
        view_func=lambda: render_template('index.html')
    )

    app.add_url_rule(
        '/about',
        endpoint='about',
        view_func=lambda: render_template('about.html')
    )

    return app
