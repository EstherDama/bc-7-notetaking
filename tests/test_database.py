import unittest
from app.database import Database
from app.functions import NoteTakingEntry
from app.note_taking import NoteTaking

"""Test Suite for testing database operations 
"""

dbmgr = Database()
dbconnect = NoteTakingEntry()
class DatabaseTests(unittest.TestCase):


    def test_search(self):     
        """ Tests whether an inserted record can be deleted
        """
        dbmgr.data_entry("test delete")
        self.assertEqual(dbmgr.search_with_limit("test delete", -1), NoteTakingEntry().search_limit("test delete" ,-1))



    def test_save(self):
        """ Tests whether an inserted record can be sought
        """ 
        dbmgr.data_entry("test record another test")      
        self.assertEqual(NoteTakingEntry().search_limit("test record another test" ,-1), dbmgr.search_with_limit("test record another test", -1))