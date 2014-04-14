from blog import application
import logging
import sqlite3
from blog.models.sqlitedb import SQLite

class BlogDB(SQLite):
    """Manages creation and modification of blog entry data into SQLite DB"""

    def _create_schema(self):
        """Create the schema for our sqlite3 db""" 
        q = ("CREATE TABLE IF NOT EXISTS " + \
             "blogs (id INTEGER PRIMARY KEY, title text, body text, epoch numeric)",)
        for x in q: self.cursor.execute(x)
        self.conn.commit()

    def add(self, title, body):
        """Adds a blog to the DB"""
        epoch = int(time.time())
        q = "INSERT INTO blogs (id, title, body, epoch) " +\
            "VALUES (NULL, ?, ?, ?)"
        try:
            self._query(q, (title, body, epoch), fetch='none')
        except Exception, e:
            raise e

    def get_latest(self, last=9999):
        """Returns all blogs"""
        q = "SELECT * FROM blogs WHERE id < ? ORDER BY id DESC LIMIT 10"
        r = self._query(q, (last,), fetch='all')
        try:
            return r
        except Exception as e:
            raise e

    def delete(self, id):
        """Deletes blog from db given an id"""
        q = "DELETE FROM blogs WHERE id=?"
        try:
            self._query(q, (id,), fetch='none')
        except Exception as e:
            raise e

    def destroy(self):
        self._destroy()
