from blog import application
from blog.controllers.web_funcs import blog_template
from blog.models.blogging import Blog
from blog.models.feature import Feature
from bottle import request

import logging

log = logging.getLogger('blog')

@application.route('/about', method='GET')
@application.route('/contact', method='GET')
def feature(**kwargs):
    path=request.urlparts.path
    log.debug(path)
    feature = Feature().get(path)
    return blog_template('feature', feature=feature)

@application.route('/', method='GET')
def home_page():
    blog = Blog()
    latest_blogs = blog.get_latest()
    blog.destroy()
    return blog_template('home_page', blogs=latest_blogs)
