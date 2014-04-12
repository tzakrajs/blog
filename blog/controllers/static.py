from blog import application
from bottle import request, static_file, template
import json
import logging
import os

log = logging.getLogger('blog')

@application.route('/<type:re:(css|js|img)>/<file:path>', method='GET')
def get_static(type, file):
    base_path = application.config.path
    return static_file(file, root='{}/static/{}/'.format(base_path, type)) 
