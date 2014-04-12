__version__ = "1.1"

import logging
import os

# add NullHandler class stub for python < 2.7
try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

# add a default handler for blog
logging.getLogger(__name__).addHandler(NullHandler())

# create a bottle stub
from bottle import Bottle, TEMPLATE_PATH
application = Bottle()

# set the template path to use
application.config.path = os.path.dirname(__file__)
TEMPLATE_PATH.append("{}/views/".format(application.config.path))
