from blog import application
from blog.models.profiledb import ProfileDB
import logging

class Profile(object):
    """Manages creation and modification of user profiles"""

    def __init__(self):
        self.profiledb = ProfileDB()

    def add(self, title, body):
        """Adds a profile"""
        try:
            self.profiledb.add(title, body)
        except Exception, e:
            raise e

    def get(self, username):
        """Returns all profiles"""
        try:
            return self.profiledb.get(username)
        except Exception as e:
            raise e

    def get_all(self):
        """Returns all profiles"""
        try:
            return self.profiledb.get_all()
        except Exception as e:
            raise e

    def delete(self, id):
        """Deletes profile given an id"""
        try:
            return self.profiledb.delete(id)
        except Exception as e:
            raise e

    def destroy(self):
        self.profiledb.destroy()
