# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from flask import Blueprint, render_template

pai_blueprint = Blueprint('pai', __name__)

__all__ = [
    'pai_blueprint',
]


@pai_blueprint.route('/pai/', methods=['GET'])
def home():
    return render_template('index.html')
