from blog import application
import logging
import sqlite3

class SQLite(object):
    """Set and get state for a given item"""

    def __init__(self):
        """Instantiates a database if none exists"""
        # instantiate logger
        self.log = logging.getLogger('blog')
        # open sqlite db
        db_path=application.config.get('sqlite.path', './db.sqlite')
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_schema()

    def _query(self, query, data, fetch='all'):
        """Runs queries against object database"""
        rows = self.cursor.execute(query, data)
        try:
            if fetch == 'all':
                return rows.fetchall()
            elif fetch == 'one':
                return rows.fetchone()
            elif fetch == 'none':
                self.conn.commit()
        except Exception, e:
            self.log.warning("miss on the db for {}: {}".format(q, e))
            raise Exception("SQLiteDB Fail on query: {}".format(query) + \
                            "excetion was {}".format(e))

    def _destroy(self):
        """Close connection to the databse"""
        self.cursor.close()
