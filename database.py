import sqlite3
import json
import collections
from datetime import datetime
import csv
from firebase import firebase

firebase = firebase.FirebaseApplication('https://flickering-inferno-4574.firebaseio.com/', None)
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
    
    # def dict_factory(cursor, row):
    #     d = {}

    #     for idx, col in enumerate(cursor.description):
    #         d[col[0]] = row[idx]
    #         return d
    #     connection = sqlite3.connect("sample.db")
    #     connection.row_factory = dict_factory
    #     cursor = connection.cursor()
    #     cursor.execute("select * from sample")
    #     # fetch all or one we'll go for all.
    #     results = cursor.fetchall()
    #     print results
    #     connection.close()

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

        rows = self.cursor.execute("SELECT * FROM notes ") #rows from the database
 
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

    # def export_to_csv(self):
        
       

    #     for row in rows:
    #         # the csv module can't handle unicode, so encode the strings
    #         row = [unicode(s).encode("utf-8") for s in row]
    #         writer.writerow(row)
    #     writer = csv.writer(csv_object)
    #     rows = self.cursor.execute("SELECT * FROM notes ")
        
    #     object_file = 'notetaking.csv'
    #     f = open(object_file, 'w')
    #     print >> f,writer




         




