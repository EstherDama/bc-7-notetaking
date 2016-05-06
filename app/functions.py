from datetime import datetime
from database import Database

obj = Database()
class NoteTakingEntry:
	

	def create_note(self, entry):
		"""
		Add text to one note instance 

		"""
		note = ''

		for i in entry:
			note += i
		obj.data_entry(entry)


	def list_limit(self, limit_passed):
		"""
		Give query results of a listnotes if no limit is given then give all

		"""
		limit = int(limit_passed)
		obj.list_with_a_limit(limit)

	def search_limit(self, query_string, limit_passed):
		"""
		Give query results of a searchnotes if no limit is given then give all

		"""		
		limit = int(limit_passed)
		obj.search_with_limit(query_string, limit)

	def view_one_note(self, note_id):
		"""
		Gives a row of one item with the specified ID 

		"""
		note = int (note_id)
		obj.view_note_for_id(note)


	def delete_one_note(self, note_id):
		"""
		Deletes a row of one item with the specified ID  

		"""
		note = int(note_id)
		obj.delete_note_for_id(note)

	def export_json(self):
		"""
		Exports to a JSON file the current state of the database 

		"""
		obj.export_to_json()


	def upload_firebase(self):
		"""
		Trasfers Data to FireBase

		"""
		obj.upload_notes()

	def import_json(self):
		"""
		Imports Data to the database from an JSON file

		"""
		alr_exist = obj.import_to_json()
		return alr_exist

	def next_list_of_notes(self, start_from, count):
		"""
		Adds feature of next to listnotes command

		"""
		where_to_start = int(start_from)
		how_many = int(count)

		obj.next_for_list_with_limit(where_to_start, how_many)

	def next_search_of_notes(self, query_string, start_from, count):
		"""
		Adds feature of next to listnotes command

		"""
		what_to_search = str(query_string)
		where_to_start = int(start_from)
		how_many = int(count)
		
		obj.next_for_search_with_limit(what_to_search, where_to_start, how_many)
	