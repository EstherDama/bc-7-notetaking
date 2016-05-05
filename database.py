import csv
import json
import sqlite3
import collections
from datetime import datetime
from firebase import firebase


firebase = firebase.FirebaseApplication('https://flickering-inferno-4574.firebaseio.com/', None)
class Database():
    #create connection

    def __init__(self):
        self.conn = sqlite3.connect('E:/andela/bc-7-notetaking/notetaking.db')
        self.cursor = self.conn.cursor()


    def create_table(self): 
        """
        Creates table NoteEntries
        Columns:
            created_at
            entry
        """
        self.cursor.execute("CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY AUTOINCREMENT,created_at TIMESTAMP, entry TEXT)")
        self.conn.commit()


    def data_entry(self, note):
        """
        Enters data

        Attr:
            created_at
            note
        """
        with self.conn:
            self.cursor.execute("INSERT INTO notes (created_at, entry) VALUES ('%s', '%s')" % (datetime.now(), note))

    
    def list_with_a_limit(self, args):
        """
        
        """
            self.cursor.execute("SELECT * FROM notes LIMIT ('%i')" % (int(args)))
            # data = c.fetchall()
            # print data
            for row in self.cursor.fetchall():
                 print '{0} : {1}, {2}'.format(row[0], row[1], row[2])

    def next_for_list_with_limit(self, args1, args2):
            self.cursor.execute("SELECT * FROM notes LIMIT '{}','{}'".format(int(args1), int(args2)))
            for row in self.cursor.fetchall():
                 print '{0} : {1}, {2}'.format(row[0], row[1], row[2])


    def search_with_limit(self, args1, args2):
            self.cursor.execute("SELECT * FROM notes WHERE entry LIKE '%{}%' LIMIT '{}'".format(args1, int(args2)))
            # data = c.fetchall()
            # print data
            for row in self.cursor.fetchall():
                 print '{0} : {1}, {2}'.format(row[0], row[1], row[2])

    def next_for_search_with_limit(self, args, args1, args2):
        self.cursor.execute("SELECT * FROM notes WHERE entry LIKE '%{}%' LIMIT '{}','{}'".format(args, int(args1), int(args2)))
        for row in self.cursor.fetchall():
             print '{0} : {1}, {2}'.format(row[0], row[1], row[2])

    def view_note_for_id(self, args):

        self.cursor.execute("SELECT * FROM notes WHERE id == ('%i')" % (int(args)))
        for row in self.cursor.fetchall():
                print '{0} : {1}, {2}'.format(row[0], row[1], row[2])

    def delete_note_for_id(self, args):

        self.cursor.execute("DELETE FROM notes WHERE id == ('%i')" % (int(args)))
        self.conn.commit()

    def upload_notes(self):
       
        rows = self.cursor.execute("SELECT * FROM notes ")

        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0]
            d['created_at'] = row[1]
            d['entry'] = row[2]
            objects_list.append(d)

        
        firebase.put('/Notes','note', objects_list)


    def export_to_json(self):

        rows = self.cursor.execute("SELECT * FROM notes ") 
 
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0]
            d['created_at'] = row[1]
            d['entry'] = row[2]
            objects_list.append(d)
         
        j = json.dumps(objects_list)
        objects_file = 'notetakingObject.json'
        f = open(objects_file,'w')
        print >> f, j


    def import_to_json(self): 
        
        json_file = "import.json"
        imported_file = json.load(open(json_file))

        for row in imported_file:
            third = row['entry']
            with self.conn:
                self.cursor.execute("INSERT INTO notes (created_at, entry) VALUES ('%s', '%s')" % (datetime.now(), third))              