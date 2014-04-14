from blog.models.auth import Auth
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
    log.debug(kwargs)
    return template(template_file, **kwargs)
