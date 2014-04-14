from blog import application
from blog.models.blogdb import BlogDB
import logging

class Blog(object):
    """Manages creation and modification of blog entrys"""

    def __init__(self):
        self.blogdb = BlogDB()

    def add(self, title, body):
        """Adds a blog"""
        try:
            self.blogdb.add(title, body)
        except Exception, e:
            raise e

    def get_latest(self, last=9999):
        """Returns all blogs"""
        try:
            return self.blogdb.get_latest()
        except Exception as e:
            raise e

    def delete(self, id):
        """Deletes blog given an id"""
        try:
            return self.blogdb.delete(id)
        except Exception as e:
            raise e

    def destroy(self):
        self.blogdb.destroy()
