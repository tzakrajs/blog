from blog import application
import logging
import sqlite3
from blog.models.authdb import AuthDB
import uuid

class Auth(object):
    """Authenticates users"""

    def __init__(self):
        self.authdb = AuthDB()
        self.log = logging.getLogger('blog')

    def authenticate(self, username, password):
        """Returns password hash for given username"""
        return self.authdb.authenticate(username, password)

    def new_session(self, username):
        """Generate new session for username"""
        sid = uuid.uuid4()
        try:
            self.authdb.new_session(sid, username)
            return sid
        except Exception, e:
            raise Exception("New Session DB Failure: {}".format(e))

    def get_session(self, sid):
        """Retrieve user data in exchange for sid"""
        try:
            data = self.authdb.get_session(sid)
            return data
        except Exception, e:
            raise Exception("Get Session DB Failure: {}".format(e))

    def kill_session(self, sid):
        """Generate new session for username"""
        try:
            self.authdb.kill_session(sid)
        except Exception, e:
            raise Exception("Kill Session DB Failure: {}".format(e))

    def new_user(self, username, password):
        """Create a new user """
        try:
            self.authdb.new_user(username, password)
        except Exception, e:
            raise Exception("New User DB Failure: {}".format(e))

    def destroy(self):
        self.authdb.destroy()
