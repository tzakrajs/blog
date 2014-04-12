from blog import application
import logging
import sqlite3

class DB(object):
    """Set and get state for a given item"""

    def __init__(self):
        """Instantiates a database if none exists"""
        # instantiate logger
        self.log = logging.getLogger('blog')
        # open sqlite db
        db_path=application.config.DB.path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_schema()

    def _create_schema(self):
        """Create the schema for our sqlite3 db""" 
        q = ["CREATE TABLE IF NOT EXISTS " + \
                 "conferences (uuid text, name text, conference_sid text)",
             "CREATE TABLE IF NOT EXISTS " + \
                 "calls (sid text, phone_number text, conference_uuid text)"]
        for x in q: self.cursor.execute(x)
        self.conn.commit()

    def get_conference_uuid(self, name):
        """Returns bridge beam conference uuid for given bridge name"""
        q = "SELECT uuid FROM conferences WHERE name=?"
        r = self.cursor.execute(q, (name,)).fetchone()
        try:
            conference_uuid = r[0]
        except TypeError as e:
            self.log.warning("miss on the db for {}: {}".format(q, e))
            conference_uuid = None
        return conference_uuid

    def get_conference_name(self, uuid):
        """Returns conference name for given bridge beam conference uuid"""
        self.log.info("looking up conference by uuid: {}".format(uuid))
        q = "SELECT name FROM conferences WHERE uuid='{}'".format(uuid)
        self.log.info('query: {}'.format(q))
        r = self.cursor.execute(q).fetchone()
        try:
            conference_name = r[0]
        except TypeError as e:
            self.log.warning("miss on the db for {}: {}".format(q, e))
            conference_name = None
        return conference_name

    def get_conferences(self):
        """
        Does a join with calls and conferences
           
        Returns rows of conference name and phone number as columns

        """
        q = "SELECT name, phone_number FROM conferences, calls " + \
            "WHERE conferences.uuid = calls.conference_uuid"
        return self.cursor.execute(q).fetchall()
                
    def create_conference(self, uuid=None, name=None):
        """Add a new conference into the conferences table"""
        if uuid and name:
            q = "INSERT INTO conferences (uuid, name) " + \
                "VALUES ('{}', '{}')".format(uuid, name) 
            self.cursor.execute(q)
            self.conn.commit()

    def add_to_conference(
            self, call_sid=None, conference_uuid=None, 
            phone_number=None):
        """Add a new call into the calls table"""
        if conference_uuid and call_sid and phone_number:
            q = "INSERT INTO calls (sid, phone_number, conference_uuid) " + \
                "VALUES (?, ?, ?)"
            self.cursor.execute(q, (call_sid, phone_number, conference_uuid))
            self.conn.commit()

    def remove_call(self, call_sid):
        """Remove call from the calls table"""
        if call_sid:
            q = "DELETE FROM calls WHERE sid='{}'".format(call_sid) 
            self.cursor.execute(q)
            self.conn.commit()

    def destroy(self):
        """Close connection to the databse"""
        self.cursor.close()
