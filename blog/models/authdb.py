from blog import application
import logging
import sqlite3
from blog.models.sqlitedb import SQLite

class AuthDB(SQLite):
    """Authenticates users against a database"""

    def _create_schema(self):
        """Create the schema for our sqlite3 db""" 
        q = ["CREATE TABLE IF NOT EXISTS " + \
             "users (username text, password text)",
             "CREATE TABLE IF NOT EXISTS " + \
             "sessions (sid text, username text)",]
        for x in q: self.cursor.execute(x)
        self.conn.commit()

    def authenticate(self, username, password):
        """Returns password hash for given username"""
        q = "SELECT COUNT(*) FROM users WHERE username=? and password=?"
        r = self._query(q, (username, password), fetch='one')
        try:
            r[0]
        except Exception as e:
            raise e

    def new_session(self, sid, username):
        """Adds a session to the DB"""
        q = "INSERT INTO sessions (sid, username) " +\
            "VALUES (?, ?)"
        try:
            self._query(q, (str(sid), username), fetch='none')
        except Exception, e:
            raise e

    def get_session(self, sid):
        """Returns session data for given sid"""
        q = "SELECT username FROM sessions WHERE sid=?"
        r = self._query(q, (sid,), fetch='one')
        try:
            return {'username': r[0],}
        except Exception as e:
            raise e

    def kill_session(self, sid):
        """Returns session data for given sid"""
        q = "DELETE FROM sessions WHERE sid=?"
        try:
            self._query(q, (sid,), fetch='none')
        except Exception as e:
            raise e

    def new_user(self, username, password):
        """Adds a user to the DB"""
        q = "INSERT INTO users (username, password) " +\
            "VALUES (?, ?)"
        try:
            self._query(q, (username, password), fetch='none')
        except Exception, e:
            raise e

    def destroy(self):
        self._destroy()
