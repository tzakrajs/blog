from blog import application
from blog.controllers.web_funcs import blog_template

import logging

log = logging.getLogger('blog')

@application.route('/', method='GET')
@application.route('/about', method='GET')
def home_page():
    return blog_template('home_page')
