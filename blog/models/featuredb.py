from blog import application
import logging
import sqlite3
from blog.models.sqlitedb import SQLite

class FeatureDB(SQLite):
    """Manages creation and modification of feature data into SQLite DB"""

    def _create_schema(self):
        """Create the schema for our sqlite3 db""" 
        q = ("CREATE TABLE IF NOT EXISTS " + \
             "features (path text, title text, body text, epoch numeric)",)
        for x in q: self.cursor.execute(x)
        self.conn.commit()

    def add(self, path, title, body):
        """Adds a feature to the DB"""
        epoch = int(time.time())
        q = "INSERT INTO features (path, title, body, epoch) " +\
            "VALUES (?, ?, ?, ?)"
        try:
            self._query(q, (path, title, body, epoch), fetch='none')
        except Exception, e:
            raise e

    def get(self, path='404'):
        """Returns feature or 404 page"""
        q = "SELECT * FROM features WHERE path = ?"
        r = self._query(q, (path,), fetch='one')
        try:
            return r
        except Exception as e:
            raise e

    def get_all(self):
        """Returns all features"""
        q = "SELECT * FROM features ORDER BY path"
        r = self._query(q, tuple(), fetch='all')
        try:
            return r
        except Exception as e:
            raise e

    def delete(self, path):
        """Deletes feature from db given a path"""
        q = "DELETE FROM features WHERE path=?"
        try:
            self._query(q, (path,), fetch='none')
        except Exception as e:
            raise e

    def destroy(self):
        self._destroy()
