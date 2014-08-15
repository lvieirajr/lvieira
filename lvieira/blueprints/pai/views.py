# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

import os
from flask import Blueprint
from pymongo import Connection
from urlparse import urlparse

pai_blueprint = Blueprint('pai', __name__)
MONGO_URL = os.environ.get('MONGOHQ_URL')

__all__ = [
    'pai_blueprint',
]


@pai_blueprint.route("/pai/", methods=["GET"])
def pai():
    connection = Connection(MONGO_URL)
    db = connection[urlparse(MONGO_URL).path[1:]]

    return db.collection_names()


