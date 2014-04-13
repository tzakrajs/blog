from blog import application
from blog.controllers.web_funcs import blog_template

import logging

log = logging.getLogger('blog')

@application.route('/user/<username>', method='GET')
def profile(username):
    return blog_template('home_page')
