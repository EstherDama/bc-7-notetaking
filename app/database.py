import json
import sqlite3
import collections
from datetime import datetime
from firebase import firebase


firebase = firebase.FirebaseApplication('https://flickering-inferno-4574.firebaseio.com/', None)
class Database():
    #create connection

    def __init__(self):
        self.connection = sqlite3.connect('notetaking.db')
        self.cursor = self.connection.cursor()


    def create_table(self): 
        """
        Creates table NoteEntries
        Columns:
            created_at
            entry
        """
        self.cursor.execute("CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY AUTOINCREMENT,created_at TIMESTAMP, entry TEXT)")
        self.connection.commit()


    def data_entry(self, note):
        """
        Enters data

        Attr:
            created_at
            note
        """
        with self.connection:
            self.cursor.execute("INSERT INTO notes (created_at, entry) VALUES ('%s', '%s')" % (datetime.now(), note))

    
    def list_with_a_limit(self, count):
        """
        Query to give a list of notes
        If No limit is passed then everything is displayed
        """
        self.cursor.execute("SELECT * FROM notes LIMIT ('%i')" % (int(count)))
        for row in self.cursor.fetchall():
             print '{0} : {1}, {2}'.format(row[0], row[1], row[2])

    def next_for_list_with_limit(self, where_to_start, how_many):
        """
        Add next functionality to list of notes which have a limit
        """
        self.cursor.execute("SELECT * FROM notes LIMIT '{}','{}'".format(int(where_to_start), int(how_many)))
        for row in self.cursor.fetchall():
             print '{0} : {1}, {2}'.format(row[0], row[1], row[2])


    def search_with_limit(self, what_to_search, how_many):
        """
        Query to give a list of notes searched by a key value
        If No limit is passed then everything is displayed
        """
        self.cursor.execute("SELECT * FROM notes WHERE entry LIKE '%{}%' LIMIT '{}'".format(what_to_search, int(how_many)))
        for row in self.cursor.fetchall():
             print '{0} : {1}, {2}'.format(row[0], row[1], row[2])

    def next_for_search_with_limit(self, what_to_search, where_to_start, count):
        """
        Add next functionality to search of notes which have a limit
        """
        self.cursor.execute("SELECT * FROM notes WHERE entry LIKE '%{}%' LIMIT '{}','{}'".format(what_to_search, int(where_to_start), int(count)))
        for row in self.cursor.fetchall():
             print '{0} : {1}, {2}'.format(row[0], row[1], row[2])

    def view_note_for_id(self, note_id):
        """
        Query for getting the row that has the specified ID
        """
        self.cursor.execute("SELECT * FROM notes WHERE id == ('%i')" % (int(note_id)))
        for row in self.cursor.fetchall():
                print '{0} : {1}, {2}'.format(row[0], row[1], row[2])

    def delete_note_for_id(self, note_id):
        """
        Query for deleting the row that has the specified ID
        """

        self.cursor.execute("DELETE FROM notes WHERE id == ('%i')" % (int(note_id)))
        self.connection.commit()

    def upload_notes(self):
        """
        Gets current data on DB and uploads to FireBase
        """
       
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
        """
        Gets current data on DB and saves in a JSON file with JSON format
        """

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

    def export_to_json_with_filename(self, filename):
        """When a file is specified
        """
        rows = self.cursor.execute("SELECT * FROM notes ") 
 
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0]
            d['created_at'] = row[1]
            d['entry'] = row[2]
            objects_list.append(d)
        j = json.dumps(objects_list)
        objects_file = str(filename)
        f = open(objects_file,'w')
        print >> f, j


    def import_to_json(self): 
        """
        Adds data to databse using a JSON file
        """
        json_file = "import.json"
        imported_file = json.load(open(json_file))

        for row in imported_file:
            third = row['entry']
            with self.connection:
                self.cursor.execute("INSERT INTO notes (created_at, entry) VALUES ('%s', '%s')" % (datetime.now(), third))     


