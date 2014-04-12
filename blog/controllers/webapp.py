from blog import application
from bottle import request, static_file, template
import json
import logging
import os

log = logging.getLogger('blog')

@application.route('/', method='GET')
@application.route('/about', method='GET')
def home_page():
    return template('home_page')

@application.route('/login', method='GET')
def login():
    return template('login_form')

@application.route('/login', method='POST')
def login():
    print "LOOOOL"
    return template('login_form')
