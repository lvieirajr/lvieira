# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

import sys
from os import environ

from lvieira.app import create_app

app = create_app()
app.run(**{
    'host': environ.get('HOST', '0.0.0.0'),
    'port': environ.get('PORT', 5000),
    'debug': len(sys.argv) > 1 and 'dev' in sys.argv[1],
    'use_reloader': len(sys.argv) > 1 and 'dev' in sys.argv[1],
})
