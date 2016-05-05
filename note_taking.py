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

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
from cmd import Cmd
from functions import NoteTakingEntry
from colorama import Fore, Back, Style


class NoteTaking(Cmd):
    """ This is a Simple Console Note Taking Application.
        This application has the following commands:
        createnote - Create a note
        viewnote  - View a single note
        deletenote - Delete a single note
        listnotes - View a formatted list of all the notes taken
        searchnotes - View a formatted list of all the notes that can be identified using the given string
        listnotes, searchnotes should have a --limit parameter for setting the number of items to display in the resulting list
        next should be invoked to see the next set of data in the current running query
        Notes are saved in a SQLite database
    """
    
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = "=>> "
        self.intro  = introduction() 
        #""  # The defaults is Usually None
    
    # @docopt_cmd
    def do_createnote(self, args):
        """ Creates a new note.
            Takes an argument  createnote <note_content>.
            Stores Created Note in Database
        """
        if len(args) == 0:
            print Fore.YELLOW + "Usage: createnote <entry>"
            print Fore.RESET
            return 0
        else:
            """Usage: createnote <entry>"""
            data = NoteTakingEntry().create_note(args)
            print Fore.GREEN + 'Your Note has been Saved'
            print Fore.RESET
            return data


    def do_viewnote(self, args):
        """ Lets you view an already existing note.
            Takes an argument  viewnote <note_id>.
            Gets the Note with the specified ID from the Database
        """
        if len(args) == 1:
            """Usage: viewnote <note_id>"""
            return NoteTakingEntry().view_one_note(args)
        else:
            print Fore.YELLOW + "Usage: viewnote <note_id>"
            print Fore.RESET
            return 0

    def do_deletenote(self, args):
        """ Lets you delete an already existing note.
            Takes an argument  deletenote <note_id>.
            Deletes the Note with the specified ID from the Database
        """
        #Should display delete after deleting
        if len(args) == 0:
            print Fore.YELLOW + "Usage: deletenote <note_id>"
            print Fore.RESET
        elif len(args):
            """Usage: deletenote <note_id>"""
            return NoteTakingEntry().delete_one_note(args)
        else:
            print Fore.YELLOW + "Usage: viewnote <note_id>"
            print Fore.RESET
            return 0

    def do_searchnote(self, args):
        """ Lets you search for an already existing note.
            Takes an argument  searchnotes <query_string>.
            View a formatted list of all the notes that can be identified by the query string
            searchnotes has a --limit parameter for setting the number of items to display in the resulting list
        """
        list_args = args.split()
        if len(list_args) == 1:
            """Usage: searchnote <query_string> [--limit]"""
            return NoteTakingEntry().search_limit(args, -1)
        elif len(list_args) == 2:
            search_string = list_args[0]
            limit_set = list_args[1]
            return NoteTakingEntry().search_limit(search_string, int(limit_set)) 
        else:
            print Fore.YELLOW + "Usage: searchnote <query_string> [--limit]" 
            print Fore.RESET
            

    def do_listnotes(self, args):
        """ Lets you view a formatted list of all the notes taken.
            Takes no argument.
            View a formatted list of all the notes that have been taken.
            listnotes has a --limit parameter for setting the number of items to display in the resulting list

        """
        if len(args) == 0:
            return NoteTakingEntry().list_note()
        elif len(args) == 1:
            try:
                global limit_set_list
                global flag_limit_list
                limit_set_list = int(args)
                flag_limit_list += int(args)
                print "You have set the limit to: {}".format(limit_set_list) 
                NoteTakingEntry().list_limit(limit_set_list)
                #Add things here
            except ValueError:
                    print Fore.YELLOW + "Usage: listnotes [--limit]"
                    print Fore.RESET
                    return 0

        else:
            """Usage: listnotes [--limit]"""
            print Fore.YELLOW + "Usage: listnotes [--limit]"
            print Fore.RESET
            return 0

    def do_export(self, args):
        """ Lets you export to a JSON file
            Takes no argument.
            Create a .js file with all the db entries
        """
        if len(args) == 0:
            """Usage: export """
            NoteTakingEntry().export_json()
            print Fore.GREEN + 'Your Have Exported The current state of the DB to the notetakingObject.json'
            print Fore.RESET
            return 0
        else:
            print Fore.YELLOW + "Usage: export"
            print Fore.RESET
            return 0


    def do_import(self, args):
        """ Lets you import from a JSON file
            Takes no argument.
            Populates table from .js file
        """
        if len(args) == 0:
            """Usage: import """
            NoteTakingEntry().import_json() 
            print Fore.GREEN + 'Your Have Imported from JSON'
            print Fore.RESET
        else:
            print Fore.YELLOW + "Usage: import"
            print Fore.RESET
            return 0


    def do_sync(self, args):
        """ Lets you synchronise with FireBase online datastore
            Takes no argument.
            Create a instance of that db in FireBase
        """
        if len(args) == 0:
            """Usage: sync """
            NoteTakingEntry().upload_firebase()
            print Fore.GREEN + 'Your Have Uploaded to FirBbase'
            print Fore.RESET
            return 0
        else:
            print Fore.YELLOW + "Usage: sync"
            print Fore.RESET
            return 0


    def do_next(self, args):
        """It is invoked to see the next set of data in the current running query"""

        if len(args) == 0:
            """Usage: sync """
            global flag_limit_list
            global limit_set_list
            if flag_limit_list != 0:
                print "this worked"
                NoteTakingEntry().next_list_of_notes(flag_limit_list, limit_set_list)
                flag_limit_list += limit_set_list 
           
        else:
            print Fore.YELLOW + "You have to do a search or list and set a limit for this to work"
            print Fore.RESET
            return 0

    def do_EOF(self, line):
        return True

    def do_quit(self, args):
        """Quits the program."""
        print "Quitting..."
        raise SystemExit




def introduction():
    c = ''
    h = ' '
    v = ' '
    
    print c + Fore.CYAN + "-" * 78 + c
    print c + "Welcome to NoteTaking Console!".center(78, h) + c
    print c + "-" * 78 + c
    print v + "NOTE TAKINNG COMMANDS".center(78) + v
    print c + "-" * 78 + c
    print v + "1 - createnote".center(78) + v
    print v + "2 - viewnote  ".center(78) + v
    print v + "3 - deletenote".center(78) + v
    print v + "4 - searchnote".center(78) + v
    print v + "5 - listnotes ".center(78) + v
    print v + "6 - export    ".center(78) + v
    print v + "6 - import    ".center(78) + v
    print v + "7 - syncnotes ".center(78) + v
    print v + "8 - next      ".center(78) + v
    print c + "-" * 78 + c
    print v + "OTHER COMMANDS".center(78) + v
    print c + "-" * 78 + c
    print v + "1 - quit".center(78) + v
    print v + "2 - help".center(78) + v
    
    # for i in range(1, 7):
    print v + " " * 78 + v
    print c + "-" * 78 + c + Fore.RESET

if __name__ == '__main__':
	NoteTaking().cmdloop()