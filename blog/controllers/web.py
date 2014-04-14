from blog import application
from blog.controllers.web_funcs import blog_template
from blog.models.blogging import Blog
from blog.models.feature import Feature

import logging

log = logging.getLogger('blog')

@application.route('/<feature>', method='GET')
def feature(**kwargs):
    path='/{}'.format(kwargs['feature'])
    feature = Feature().get(path)[0]
    return blog_template('feature', feature=feature)

@application.route('/', method='GET')
def home_page():
    blog = Blog()
    latest_blogs = blog.get_latest()
    blog.destroy()
    return blog_template('home_page', blogs=latest_blogs)
