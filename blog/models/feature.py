from blog import application
from blog.models.featuredb import FeatureDB
import logging

class Feature(object):
    """Manages creation and modification of feature entrys"""

    def __init__(self):
        self.featuredb = FeatureDB()

    def add(self, patch, title, body):
        """Adds a feature"""
        try:
            self.featuredb.add(title, body)
        except Exception, e:
            raise e

    def get_all(self):
        """Returns all features"""
        try:
            return self.featuredb.get_all()
        except Exception as e:
            raise e

    def get(self, path):
        """Returns features given a path"""
        try:
            return self.featuredb.get(path)
        except Exception as e:
            raise e

    def delete(self, path):
        """Deletes feature given a path"""
        try:
            return self.featuredb.delete(path)
        except Exception as e:
            raise e

    def destroy(self):
        self.featuredb.destroy()
