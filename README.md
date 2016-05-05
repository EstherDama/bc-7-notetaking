# bc-7-notetaking
## Synopsis

At the top of the file there should be a short introduction and/ or overview that explains **what** the project is. This description should match descriptions added for package managers (Gemspec, package.json, etc.)

## Code Example

Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.

## Motivation

A short description of the motivation behind the creation and maintenance of the project. This should explain **why** the project exists.

## Installation

Provide code examples and explanations of how to get the project.

## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## Tests

Describe and show how to run the tests with code examples.

## Contributors

Let people know how they can dive into the project, include important links to things like issue trackers, irc, twitter accounts if applicable.

## License

A short snippet describing the license (MIT, Apache, etc.)

``Scrible`` Python *Console application* for taking notes
======================================================================

    New in version 0.0.3:

    - Beautiful ui with added commands such as ``sync`` for automatic 
      synchronization of notes

    New in version 0.0.2:

    - Better listing and searching options with ``--limit`` to get
      specific number of items


**Scrible** enables you create short and descriptive notes with cloud backup
*easily*:


Launching program
======================================================================

    scrible --start

.. code:: python

    """Scrible.

    Usage:
	    createnote  (<note_title>) [-m]
	    viewnote    (<note_id>) [-m]
	    deletenote  (<note_id> | -a)
	    searchnotes (<query_string>) [(--limit <items>)]
	    viewnote    (<note_id>)
	    listnotes   [(--limit <items>)]
	    next
	    export      (<filename>)
	    import      (<filename>)
	    sync 
	    scrible (-s | --start)
	    scrible (-h | --help | --version)
	Options:
	    -s, --start  Interactive Mode
	    -h, --help  Show this screen and exit.
	    -m          Starts creating note body

    """

As you can see, the commands to use are few and easy to remember.

Installation
======================================================================

From the terminal use `pip <http://pip-installer.org>`_ or easy_install::
Aftwerwards copy the database to the install directory `scribler.db`

    pip install -e git+https://github.com/jaxtreme01/Scrible#egg=scrible

Testing
======================================================================

You can run unit tests preferably by installing nosetest and run from root of the folder:

    nosetests

Usage pattern format
----------------------------------------------------------------------

**Usage pattern** depends on the command you want to execute

- View specific notes 
.. code:: python

	viewnote (<note_id>) [-m]

- Create note with just title 
.. code:: python 

	createnote  (<note_title>)

- Create note with title and body
.. code:: python 

	createnote  (<note_title>) [-m]

- Delete notes
.. code:: python 

	deletenote  (<note_id> | -a)

- Search notes
.. code:: python 

	searchnotes (<query_string>) [(--limit <items>)]

- List notes
.. code:: python 

	listnotes [(--limit <items>)]

- Import notes
.. code:: python 

	import (<filename>)

- Export notes
.. code:: python 

	export (<filename>)

- Manually sync notes

	sync 










