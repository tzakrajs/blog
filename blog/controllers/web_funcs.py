from blog.models.auth import Auth
from blog.models.feature import Feature
from bottle import request, template
import logging

log = logging.getLogger('blog')

def blog_template(template_file, **kwargs):
    auth = Auth()
    sid = request.get_cookie('SID')
    try:
        if sid:
            session_data = auth.get_session(sid)
            username = session_data.get('username')
            kwargs = dict({'username': username}, **kwargs)
        else:
            raise Exception("missing SID cookie")
    except Exception, e:
        log.warning("Exception caught: user has no session - {}".format(e))
    feature = Feature()
    menu = (('/', 'Home'),)
    for (path, title, body, time) in feature.get_all():
        menu += ((path, title),)
    feature.destroy()
    kwargs = dict({'menu': menu}, **kwargs)
    kwargs = dict({'r_path': request.urlparts.path}, **kwargs)
    return template(template_file, **kwargs)
