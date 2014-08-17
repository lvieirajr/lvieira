# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from pymongo import Connection

from .settings import MONGOHQ_URL, DB_NAME

__all__ = [
    'get_db'
]

db = Connection(MONGOHQ_URL)[DB_NAME]


def get_db():
    return db
