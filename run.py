# coding: UTF-8
from __future__ import absolute_import, division, print_function, unicode_literals

import os
import sys

from lvieira.main_app import create_app

mode = sys.argv[1] if len(sys.argv) > 1 else 'development'

app = create_app(mode=mode)

config = app.config.get_namespace('RUN_')
config['port'] = os.environ.get('PORT', 5000)

app.run(**config)