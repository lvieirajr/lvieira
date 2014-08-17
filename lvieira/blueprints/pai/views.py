# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from flask import Blueprint, render_template_string

from lvieira.database import get_db


__all__ = [
    'pai_blueprint',
]

pai_blueprint = Blueprint('pai', __name__)
db = get_db()


@pai_blueprint.route("/pai/", methods=["GET"])
def home():
    return render_template_string('<br>'.join(db.collection_names()))


