from blog import application
from bottle import request, static_file, template
import json
import logging
import os

log = logging.getLogger('blog')

@application.route('/', method='GET')
def home_page():
    return template('home_page')

