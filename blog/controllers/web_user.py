from blog import application
from blog.controllers.web_funcs import blog_template
from blog.models.profile import Profile

import logging

log = logging.getLogger('blog')

@application.route('/user/<username>', method='GET')
def profile(username):
    profile = Profile().get(username)
    return blog_template('profile', profile=profile)
