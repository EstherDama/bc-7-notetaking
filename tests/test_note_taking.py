"""Test Suite for Note Taking."""
from unittest import TestCase
from app.note_taking import NoteTaking



class NoteTakingTestCase(TestCase): #all methods that have the word test then it shoulld run!!!
	''' Test Case for NoteTaking'''

	# def  test_create_note(self):
	# 	'''Test for creating a note with a note content'''
 #        """ Tests whether an inserted record can be deleted
 #        """
 #        note = NoteTaking().do_createnote("test createnote command")       
 #        self.assertEqual(note[2], "test createnote command")

	
	def  test_create_note_without_input(self):
		'''Test for creating a note without any note content'''
		note = NoteTaking().do_createnote()       
        # self.assertEqual(note, 0)


	# def test_view_note(self):
	# 	'''Test for viewing note when it is given an ID as input'''
	# 	note = NoteTaking().createnote("test viewnote command")
	# 	view = NoteTaking().viewnote(note[0])       
 #        self.assertEqual(view[2], "test createnote command")

	# def test_view_note_without_id(self):
	# 	'''Test for viewing note when it is given an ID as input'''
	# 	view = NoteTaking().viewnote()       
 #        self.assertEqual(view, 0)
	

	# def test_delete_note(self):
	# 	'''Test for delete note when it is given an ID as input'''
	# 	note = NoteTaking().createnote("test deletenote command")
	# 	view = NoteTaking().deletenote(note[0])       
 #        self.assertEqual(view, 0)

	# def test_delete_note_without_id(self):
	# 	'''Test for delete note when it is given an ID as input'''
	# 	view = NoteTaking().deletenote()       
 #        self.assertEqual(view, 0)

		
	# def test_search_note_without_limit(self):
	# 	'''Test for search a note when it is given a query_string as an input '''

	# def test_search_note_with_limit(self):
	# 	'''Test for search a note when it is given a query_string as an input '''

	# def test_next_for_search_note(self):
	# 	'''Test for search a note when it is given a query_string as an input '''
		
	# def test_search_notes_without_query_string(self):
	# 	'''Test for list of notes when it has stored'''

	# def test_list_note_without_limit(self):
	# 	'''Test for search a note when it is given a query_string as an input '''

	# def test_list_note_with_limit(self):
	# 	'''Test for search a note when it is given a query_string as an input '''

	# def test_next_for_list_note(self):
	# 	'''Test for search a note when it is given a query_string as an input '''

	# def test_export_to_JSON(seif):
	# 	'''Test for exporting to JSON file'''

	# def test_export_to_JSON_with_arguement(seif):
	# 	'''Test for exporting to JSON file'''

	# def test_import_from_JSON(seif):
	# 	'''Test for importing to JSON file'''

	# def test_import_from_JSON_with_arguement(seif):
	# 	'''Test for importing to JSON file'''

	# def test_sync_to_firebase(seif):
	# 	'''Test for exporting to JSON file'''

	# def test_sync_to_firebase_with_arguement(seif):
	# 	'''Test for exporting to JSON file'''

