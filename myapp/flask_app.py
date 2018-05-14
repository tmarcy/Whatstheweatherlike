
from flask import Flask
from flask_wtf.csrf import CSRFProtect

import appengine_config
import myapp.app_config
import logging

app = Flask(__name__)
app.config.from_object(__name__)


if appengine_config.GAE_DEV:
    logging.info('using a dummy secret key')
    app.secret_key = 'my-secrete-key'
    app.debug = True
else:
    app.secret_key = myapp.app_config.app_secure_key

DEBUG = True
csrf = CSRFProtect(app)
