import sqlite3
from datetime import datetime

class Database:
    #create connection
    def __init__(self):
        self.conn = sqlite3.connect('E:/andela/bc-7-notetaking/notetaking.db')
        self.cursor = self.conn.cursor()
        # self.create_table()


    def create_table(self):
        """
        Creates table Note Entries
        Columns:
            created_at
            entry
        """
        self.cursor.execute("CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY AUTOINCREMENT,created_at TIMESTAMP, entry TEXT)")
        self.conn.commit()
        # c.close()
        # conn.close()

    #insert data into table
    def data_entry(self, note):
        """
        Enters data

        Attr:
            created_at
            note
        """
        with self.conn:
            #insert a row of data
            self.cursor.execute("INSERT INTO notes (created_at, entry) VALUES ('%s', '%s')" % (datetime.now(), note))
            # conn.commit()


    def list_all_from_db(self):
            self.cursor.execute('SELECT * FROM notes')
            # data = c.fetchall()
            # print data
            for row in self.cursor.fetchall():
                 print '{0} : {1}, {2}'.format(row[0], row[1], row[2])

    def search_for_string(self, args):
        a = args
        # import ipdb
        # ipdb.set_trace()
        self.cursor.execute("SELECT * FROM notes WHERE entry LIKE '%{}%'".format(args))


        for row in self.cursor.fetchall():
            if a in row[2]:
                print '{0} : {1}, {2}'.format(row[0], row[1], row[2])

    def view_note_for_id(self, args):

        self.cursor.execute("SELECT * FROM notes WHERE id == ('%i')" % (int(args)))
        for row in self.cursor.fetchall():
                print '{0} : {1}, {2}'.format(row[0], row[1], row[2])

    def delete_note_for_id(self, args):

        self.cursor.execute("DELETE FROM notes WHERE id == ('%i')" % (int(args)))
        self.conn.commit()

