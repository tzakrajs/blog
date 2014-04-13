from blog import application
from blog.controllers.web_funcs import blog_template
from blog.models.auth import Auth

from bottle import response, request, template
import logging

log = logging.getLogger('blog')

@application.route('/login', method='GET')
def login():
    """Give the login form"""
    return blog_template('login_form')

@application.route('/login', method='POST')
def login_post():
    """Handles user submissions of login form"""
    auth = Auth()
    username = request.POST['username']
    password = request.POST['password']
    try:
        auth.authenticate(username, password)
    except Exception, e:
        auth.destroy()
        log.warning("User: {} failed to login ".format(username) + \
                    "with password: {}".format(password))
        return blog_template('login_form')
    try:
        sid = auth.new_session(username)
        response.set_cookie('SID', str(sid))
        log.debug("User: {} has recieved a session".format(username))
    except:
        log.warning("User: {} failed to spawn session ".format(username) + \
                    "with sid: {}".format(sid))
    finally:
        auth.destroy()
    response.add_header('Location', '/')
    response.status = 302

@application.route('/logout', method='GET')
def logout():
    """Destroys user session and redirects to home"""
    auth = Auth()
    sid = request.get_cookie('SID')
    if sid:
        auth.kill_session(sid)
        auth.destroy()
        response.delete_cookie('SID')
    response.add_header('Location', '/')
    response.status = 302
