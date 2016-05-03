"""Test Suite for Note Taking."""
from unittest import TestCase
from note_taking import NoteTaking

class NoteTakingTestCase(TestCase): #all methods that have the word test then it shoulld run!!!
	''' Test Case for NoteTaking'''

	def  test_create_note(self):
		'''Test for creating a note with a note content'''
		first_note = NoteTaking('This is just a simple note!!')
        self.assertIsInstance(first_note, NoteTaking, 
        					 	msg='The object should be an instance of the `NoteTaking` class')

    def  test_empty_create_note(self):
		'''***Test for creating a note without any note content'''
		second_note = NoteTaking()
        self.assertEqual('', 'Do you want to save an Empty Note?',
                         msg='The second_note should not be an instant of a class')

	def test_view_note(self):
		'''Test for viewing note when it is given an ID as input'''
		s

	def test_delete_note(self):
		'''Test for delete note when it is given an ID as input'''
		

	def test_search(self):
		'''Test for search a note when it is given a query_string as an input '''
		
	
	def test_list_notes(self):
		'''Test for list of notes when it has stored'''
		

