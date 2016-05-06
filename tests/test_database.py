# import unittest
# from database import Database
# from functions import NoteTakingEntry

# """Test Suite for testing database operations 
# """

# dbmgr = Database()
# dbconnect = NoteTakingEntry()
# class DatabaseTests(unittest.TestCase):


#     def test_delete(self):     
#         """ Tests whether an inserted record can be deleted
#         """
#         dbmgr.data_entry("testdelete")
#         cursor = dbmgr.search_with_limit("testdelete", -1)
#         note = dbmgr.delete_note_for_id(cursor[0])
#         self.assertGreater(note, 0)



#     def test_save(self):
#         """ Tests whether an inserted record can be sought
#         """ 
#         note = dbmgr.data_entry("testrecordsave")       
#         notes = dbmgr.search_with_limit("testrecordsave", -1)
#         self.assertEqual(notes[2], "testrecordsave")

#         """ Tests whether an inserted record can be sought
#         """