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

	def list_limit(self, args):
		obj = Database()
		limit = int(args)
		obj.list_with_a_limit(limit)

	def search_limit(self, args1, args2):
		obj = Database()
		limit = int(args2)
		obj.search_with_limit(args1, limit)

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

	def export_json(self):
		obj = Database()
		obj.export_to_json()

	# def export_csv(self):
	# 	obj = Database()
	# 	obj.export_to_csv()

	def upload_firebase(self):
		obj = Database()
		obj.upload_notes()

	def import_json(self):
		obj = Database()
		alr_exist = obj.import_to_json()
		return alr_exist

	def next_list_of_notes(self, args1, args2):
		arg1 = int(args1)
		arg2 = int(args2)
		# (" ".join(args['<entry>']))
		
		obj = Database()
		obj.next_for_list_with_limit(arg1,arg2)

	def next_search_of_notes(self, args, args1, args2):
		args = str(args)
		arg1 = int(args1)
		arg2 = int(args2)
		# (" ".join(args['<entry>']))
		
		obj = Database()
		obj.next_for_search_with_limit(arg1,arg2)
	