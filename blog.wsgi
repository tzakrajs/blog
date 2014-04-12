#!/usr/bin/env python
import os
import sys

# do some magic if we are running wsgi
try:
    import mod_wsgi

    # Change working directory so relative paths (and template lookup) work again
    os.chdir(os.path.dirname(__file__))

    # Add working directory to paths
    sys.path.append(os.path.dirname(__file__))
except:
    pass

from blog_app import application
import logging

# config log format
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)-21s %(levelname)s %(name)s (%(funcName)-s) %(process)d:%(thread)d - %(message)s',
                    filename='lol.log')

# global variables config
application.config.load_config('./config.ini')

# setup the blog server
from blog_app.controllers import *

# start the bottle server if we aren't running as wsgi

try:
    import mod_wsgi
    pass
except:
    host = application.config.get('server.host', '0.0.0.0')
    port = application.config.get('port', '8080')
    application.run(host=host, port=port)
