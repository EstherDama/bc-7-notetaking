# bc-7-notetaking
Python ``NoTa`` *Console application* 
======================================================================

## Introduction
*  **`NoTa`** is a Python Console Application.
*  These are its features;
  *  Allows the creation of notes
  *  Allows the viewing of a note using its specific id
  *  Allows the deleting a note using its specific id
  *  Allows search of notes with a search string
  *  Allows listing of all notes or a few notes set by your limit
  *  Allows exporting to a JSON file
  *  Image importing from a JSON file
  *  Image syncing of notes with online datastore
  *  Allows for next to show next results of the currently executing query 

**NoTa** allows you quickly create short notes, allows for easy manipulation of the notes and back-up notes on FireBase.


Commands for the program
======================================================================

```Python
"""
This shows how to use the various commands on NoteTaking Console Application
Usage:
    notetaking createnote <entry>
    notetaking viewnote <note_id>
    notetaking deletenote <note_id>
    notetaking searchnote <query_string> [--limit]
    notetaking listnotes [--limit]
    notetaking export 
    notetaking import 
    notetaking sync 
"""
```
As you can see, the commands to use are few and easy to remember.

Installation
======================================================================
From the requirements.txt install all the modules
This is done by use of `pip <module>` on the Terminal
Aftwerwards copy the database to the install directory `notetaking.db`

Testing
======================================================================

You can run unit tests preferably by installing nosetest and run from root of the folder:

    nosetests
Ran 2 tests and they are OK


Usage pattern format
----------------------------------------------------------------------

**Usage pattern** depends on the command you want to execute

- View a specific note 
```
	viewnote <note_id>
```

- Create a single note 
```
	createnote <entry>
```


- Delete a specific note
``` 

	deletenote <note_id>
```
- Search notes with a query string and optional limit
``` 

	searchnote <query_string> [--limit]
```
- List all notes or optional limit of number of notes
``` 

	listnotes [--limit]
```
- Import notes from a JSON file
``` 

	import 
```
- Export notes to a JSON file
``` 

	export
``` 

- Manually sync notes with Firebase
```
	sync 
```