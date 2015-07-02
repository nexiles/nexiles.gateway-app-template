.. _quickinstall-mac:

Quickinstall (Apple Mac)
========================

Abstract
--------

This is the **quick installation** documentation.  This is a tersely written documentation for experienced
developers.  This documentation targets developers using **Apple Mac** computers.

Installing Prerequisites
------------------------

Install Homebrew_ -- this is a prerequisite, for more information see their web site.

Install tools::

	$ brew install python
	$ brew install node
	$ npm install -g grunt-cli

Python packages::

	$ pip install virtualenv

ExtJs_ -- we need `Sencha Command`_ to build apps.  Please follow the instructions there to install
the tool.  Pleas make sure to use ExtJs_ version **5.x**.  On my machine, `sencha` gives me the following
output::

	$ sencha
	Sencha Cmd v6.0.0.202
	Sencha Cmd provides several categories of commands and some global switches. In
	most cases, the first step is to generate an application based on a Sencha SDK
	such as Ext JS or Sencha Touch:

	    sencha -sdk /path/to/sdk generate app MyApp /path/to/myapp

	Sencha Cmd supports Ext JS 4.1.1a and higher and Sencha Touch 2.1 and higher.

	To get help on commands use the help command:

	    sencha help generate app

	For more information on using Sencha Cmd, consult the guides found here:

	http://docs.sencha.com/cmd/


	Options
	  * --beta, -be - Enable beta package repositories
	  * --cwd, -cw - Sets the directory from which commands should execute
	  * --debug, -d - Sets log level to higher verbosity
	  * --info, -i - Sets log level to default
	  * --nologo, -n - Suppress the initial Sencha Cmd version display
	  * --plain, -pl - enables plain logging output (no highlighting)
	  * --quiet, -q - Sets log level to warnings and errors only
	  * --sdk-path, -sd - The location of the SDK to use for non-app commands
	  * --strict, -st - Treats warnings as errors, exiting with error if any warnings are present
	  * --time, -ti - Display the execution time after executing all commands

	Categories
	  * app - Perform various application build processes
	  * compass - Wraps execution of compass for sass compilation
	  * compile - Compile sources to produce concatenated output and metadata
	  * cordova - Quick init Support for Cordova
	  * fs - Utility commands to work with files
	  * generate - Generates models, controllers, etc. or an entire application
	  * manifest - Extract class metadata
	  * package - Manages local and remote packages
	  * phonegap - Quick init support for PhoneGap
	  * repository - Manage local repository and remote repository connections
	  * space - Commands for interacting with Sencha Space.
	  * theme - Commands for low-level operations on themes
	  * web - Manages a simple HTTP file server

	Commands
	  * ant - Invoke Ant with helpful properties back to Sencha Cmd
	  * audit - Search from the current folder for Ext JS frameworks and report their license
	  * build - Builds a project from a legacy JSB3 file.
	  * config - Load a properties file or sets a configuration property
	  * help - Displays help for commands
	  * js - Executes arbitrary JavaScript file(s)
	  * upgrade - Upgrades Sencha Cmd
	  * which - Displays the path to the current version of Sencha Cmd


Clone Template, First Time Setup
--------------------------------

Setup project directory
~~~~~~~~~~~~~~~~~~~~~~~

Clone the template repository, cd into the repo and do::

	$ virtualenv .
	$ . ./bin/activate
	$ pip install -r requirements.txt
	$ fab init
	Initializing repo
	    Installing node modules ...
	    Compiling coffee scripts ...
	    Initializing sencha framework ...
	    Building application ...

	Done.

This needs to be done only **once**.

Build Application
-----------------

Always activate the virtualenv_!

Change directory to the repo dir and do::

	$ . ./bin/activate
	$ fab
	Building for production
	   installing node modules ...
	   compiling CoffeScript ...
	   building app ...
	Packaging app (production)
	Built package: /Users/seletz/develop/nexiles/nexiles.gateway-app-template/build/AppTemplate-production.zip .
	Building documentation

	Done.


.. _Homebrew: http://brew.sh/
.. _Node: https://nodejs.org/
.. _virtualenv: https://virtualenv.pypa.io/en/latest/
.. _ExtJS: https://www.sencha.com/products/extjs/
.. _Sencha Command: https://www.sencha.com/products/extjs/#sencha-cmd
.. _Grunt: http://gruntjs.com/
.. _CoffeeScript: http://coffeescript.org/
.. _Fabric: http://www.fabfile.org/
.. _Sphinx: http://sphinx-doc.org/
.. _Python: http://www.python.org
.. _nexiles gateway: http://nexiles.com/products
.. _PTC Windchill: http://www.ptc-solutions.de/produkte/ptc-windchill/ptc-windchill-102.html
.. _us: mailto:info@nexiles.com?subject=nexiles.gateway%20apps%20request%20for%20information&cc=se@nexiles.de