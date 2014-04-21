from blog import application
import logging
import sqlite3
from blog.models.sqlitedb import SQLite

class ProfileDB(SQLite):
    """Manages creation and modification of user profile data into SQLite DB"""

    def _create_schema(self):
        """Create the schema for our sqlite3 db""" 
        q = ("CREATE TABLE IF NOT EXISTS " + \
             "profiles (username text, body text, epoch numeric)",)
        for x in q: self.cursor.execute(x)
        self.conn.commit()

    def add(self, username, title, body):
        """Adds a profile to the DB"""
        epoch = int(time.time())
        q = "INSERT INTO profiles (username, title, body, epoch) " +\
            "VALUES (?, ?, ?, ?)"
        try:
            self._query(q, (username, title, body, epoch), fetch='none')
        except Exception, e:
            raise e

    def get(self, username):
        """Returns a profile for given username"""
        q = "SELECT * FROM profiles where username = ?"
        r = self._query(q, (username,), fetch='one')
        try:
            return r
        except Exception as e:
            raise e

    def get_all(self):
        """Returns all profiles"""
        q = "SELECT * FROM profiles"
        r = self._query(q, tuple(), fetch='all')
        try:
            return r
        except Exception as e:
            raise e

    def delete(self, user):
        """Deletes profile from db given an id"""
        q = "DELETE FROM profiles WHERE user=?"
        try:
            self._query(q, (user,), fetch='none')
        except Exception as e:
            raise e

    def destroy(self):
        self._destroy()
