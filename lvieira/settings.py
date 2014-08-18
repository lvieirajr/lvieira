# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from os import path, environ


PROJECT_ROOT = path.abspath(path.dirname(__file__))

SECRET_KEY = environ.get('SECRET_KEY')

MONGO_URI = environ.get('MONGOHQ_URL')
MONGO_DBNAME = MONGO_URI.split('/')[-1]
MONGODB_SETTINGS = {
    'db': MONGO_DBNAME,
    'host': MONGO_URI
}


