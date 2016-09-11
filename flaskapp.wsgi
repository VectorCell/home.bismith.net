#!/usr/bin/env python3

import sys
import logging

logging.basicConfig(stream=sys.stderr)
if '/var/www/home/' not in sys.path:
    sys.path.insert(0, '/var/www/home/')
if '/var/www/home/app/' not in sys.path:
    sys.path.insert(1, '/var/www/home/app/')

from app import app as application
application.secret_key = 'secret'