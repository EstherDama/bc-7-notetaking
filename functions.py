from datetime import datetime
from database import Database

class NoteTakingEntry:
	

	def create_note(self, args):
		"""
		Add text to one note instance 
		
		Args:
			title - string containing the title of your journal
		"""

		note = ''
		# (" ".join(args['<entry>']))

		for i in args:
			note += i
		
		obj = Database()
		obj.data_entry(note)

	def list_note(self):
		obj = Database()
		obj.list_all_from_db()

	def search_string(self, args):
		note = ''
		# (" ".join(args['<entry>']))

		for i in args:
			note += i
		
		obj = Database()
		obj.search_for_string(note)

	def view_one_note(self, args):
		note = int(args)
		# (" ".join(args['<entry>']))
		
		obj = Database()
		obj.view_note_for_id(note)


	def delete_one_note(self, args):
		note = int(args)
		# (" ".join(args['<entry>']))
		
		obj = Database()
		obj.delete_note_for_id(note)

