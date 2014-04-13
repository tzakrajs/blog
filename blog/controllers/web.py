from blog import application
from bottle import template
import logging

log = logging.getLogger('blog')

@application.route('/', method='GET')
@application.route('/about', method='GET')
def home_page():
    return template('home_page')

