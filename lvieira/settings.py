# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

from os import path, environ


PROJECT_ROOT = path.abspath(path.dirname(__file__))
MONGOHQ_URL = environ.get('MONGOHQ_URL')
DB_NAME = MONGOHQ_URL.split('/')[-1]
