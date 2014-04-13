from blog import application
from bottle import response, request, template
from blog.models.auth import Auth
import logging

log = logging.getLogger('blog')

@application.route('/login', method='GET')
def login():
    """Give the login form"""
    return template('login_form')

@application.route('/login', method='POST')
def login_post():
    """Handles user submissions of login form"""
    auth = Auth()
    username = request.POST['username']
    password = request.POST['password']
    try:
        auth.authenticate(username, password)
    except Exception, e:
        log.warning("User: {} failed to login ".format(username) + \
                    "with password: {}".format(password))
        return template('login_form')
    try:
        sid = auth.new_session(username)
        response.add_header('Set-Cookie', 'SID={}'.format(sid))
    except:
        log.warning("User: {} failed to spawn session ".format(username) + \
                    "with sid: {}".format(sid))
    response.add_header('Location', '/')
    response.status = 302

@application.route('/logout', method='GET')
def logout():
    """Destroys user session and redirects to home"""
    auth = Auth()
    sid = request.cookies.get('SID')
    if sid:
        auth.kill_session(sid)
        response.delete_cookie('SID')
    response.add_header('Location', '/')
    response.status = 302
