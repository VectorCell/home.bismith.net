#!/usr/bin/env python3

import sys
import os
import logging

dir_base = os.path.dirname(os.path.realpath(__file__))
if dir_base[-1] != '/':
	dir_base += '/'
dir_app = dir_base + 'app/'

logging.basicConfig(stream=sys.stderr)
if dir_base not in sys.path:
    sys.path.insert(0, dir_base)
if dir_app not in sys.path:
    sys.path.insert(1, dir_app)

from app import app as application
application.secret_key = 'secret'