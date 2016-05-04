#Things to add
# Create a syncnotes command for automatically synchronising notes with online datastore like Firebase or Parse (extra credit)
# The Notes should be exportable and importable as CSV or JSON.


"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    journal entry <entry>
    journal (-i | --interactive)
    journal (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
from cmd import Cmd
# from docopt import docopt, DocoptExit
from functions import NoteTakingEntry


# def docopt_cmd(func):
#     """
#     This decorator is used to simplify the try/except block and pass the result
#     of the docopt parsing to the called action.
#     """
#     def fn(self, arg):
#         try:
#             opt = docopt(fn.__doc__, arg)

#         except DocoptExit as e:
#             # The DocoptExit is thrown when the args do not match.
#             # We print a message to the user and the usage block.

#             print('Invalid Command!')
#             print(e)
#             return

#         except SystemExit:
#             # The SystemExit exception prints the usage for --help
#             # We do not need to do the print here.

#             return

#         return func(self, opt)

#     fn.__name__ = func.__name__
#     fn.__doc__ = func.__doc__
#     fn.__dict__.update(func.__dict__)
#     return fn


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
            print "Please Enter Data for Note"
            return 0
        else:
            """Usage: entry <entry>..."""
            data = NoteTakingEntry().create_note(args)
            print 'Your Note has been Saved'
            return data


    def do_viewnote(self, args):
        """ Lets you view an already existing note.
            Takes an argument  viewnote <note_id>.
            Gets the Note with the specified ID from the Database
        """
        if len(args) == 0:
            print "Please Specify the ID for the note you want to view"
            return 0
        else:
            return NoteTakingEntry().view_one_note(args)

    def do_deletenote(self, args):
        """ Lets you delete an already existing note.
            Takes an argument  deletenote <note_id>.
            Deletes the Note with the specified ID from the Database
        """
        #Should display delete after deleting
        if len(args) == 0:
            print "Please Specify the ID for the note you want to delete"
        else:
            return NoteTakingEntry().delete_one_note(args)

    def do_searchnote(self, args):
        """ Lets you search for an already existing note.
            Takes an argument  searchnotes <query_string>.
            View a formatted list of all the notes that can be identified by the query string
            searchnotes has a --limit parameter for setting the number of items to display in the resulting list
        """
        if len(args) == 0:
            print "Please Enter Search String"
        else:
            return NoteTakingEntry().search_string(args)
            

    def do_listnotes(self, args):
        """ Lets you view a formatted list of all the notes taken.
            Takes no argument.
            View a formatted list of all the notes that have been taken.
            listnotes has a --limit parameter for setting the number of items to display in the resulting list

        """
        if len(args) == 0:
            return NoteTakingEntry().list_note()
        else:
            print "List Does not accept any arguments"
            return 0

    def do_next(self, args):
        """It is invoked to see the next set of data in the current running query"""
        if len(args) == 0:
            name = 'Stranger'
        else:
            name = args
        print "Hello, %s" % name

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
    print c + "-" * 78 + c
    print c + "Welcome to NoteTaking Console!".center(78, h) + c
    print c + "-" * 78 + c
    print v + "NOTE TAKINNG COMMANDS".center(78) + v
    print c + "-" * 78 + c
    print v + "1 - createnote".center(78) + v
    print v + "2 - viewnote  ".center(78) + v
    print v + "3 - deletenote".center(78) + v
    print v + "4 - searchnote".center(78) + v
    print v + "5 - listnotes ".center(78) + v
    print c + "-" * 78 + c
    print v + "OTHER COMMANDS".center(78) + v
    print c + "-" * 78 + c
    print v + "1 - quit".center(78) + v
    print v + "2 - help".center(78) + v
    
    for i in range(1, 7):
        print v + " " * 78 + v
    print c + "-" * 78 + c

# opt = docopt(__doc__, sys.argv[1:])

if __name__ == '__main__':
	NoteTaking().cmdloop()

# if opt['--interactive']:
#     NoteTaking().cmdloop()

# print(opt)