#!/usr/bin/env python
import os
import sys
import logging

def setup():
    # config log format
    format="%(asctime)-21s %(levelname)s %(name)s (%(funcName)-s) " + \
           "%(process)d:%(thread)d - %(message)s"
    logging.basicConfig(level=logging.DEBUG,
                        format=format,
                        stream=sys.stderr)
    
    # global variables config
    application.config.load_config('blog.cfg')
    
# mod_wsgi setup
try:
    import mod_wsgi

    # Change working directory so relative paths (and template lookup) work again
    os.chdir(os.path.dirname(__file__))

    # Add working directory to paths
    sys.path.append(os.path.dirname(__file__))

    # setup the blog server
    from blog import application
    setup()
    from blog.controllers import *

# bottle setup
except:
    # setup the blog server
    from blog import application
    setup()
    from blog.controllers import *

    host = application.config.get('bottle.host', '0.0.0.0')
    port = application.config.get('bottle.port', '8080')
    application.run(host=host, port=port)
