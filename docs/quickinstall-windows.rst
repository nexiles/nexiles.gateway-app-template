.. _quickinstall-win:

Quickinstall (Windows)
======================

Abstract
--------

This is the **quick installation** documentation.  This is a tersely written documentation for experienced
developers.  This documentation targets developers using **Windows** computers.

Unfortunately, the Fabric_ tools is not supported on Windows, so you need to do build steps manually.  But they're
easy and you can always create some bat files.

.. note:: Windows is not the author's main development platform.  If you spot some errors, stupidity or have comments
   please contact me_.


Installing Prerequisites
------------------------

.. note:: I use Chokolatey_ -- This is very opinionated, and you need admin access to your machine.  If you
   know a better/alternate way contact me_, or please issue a pull request on GitHub.

Install Chokolatey_ -- this makes installing tools on Windows actually bearable.

.. note:: Please make **sure** you use Chokolatey_ in a **admin shell**.

Install tools::

	C:> choco install git

Optionally install GOW_ -- a light-weight set of UNIX like tools::

	C:> choco install GOW

Node.js
~~~~~~~

Install Node_ and the node package manager `npm`::

	C:> choco install nodejs.install

Close and reopen the shell, and::

	C:> npm install -g grunt-cli

Python Setup
~~~~~~~~~~~~

Install Python::

	C:> choco install python2

At the time of this writing, Chokolatey_ installs Python_ to `C:/tools/python2.x.x` and adds this directory
to the `PATH`.  But unfortunately, it doesn't add the `Scripts` directory within the python installation to the
`PATH`.  Make **sure** thyt you correct thos before you continue.

Python packages::

	C:> pip install virtualenv

ExtJs
~~~~~

ExtJs_ -- we need `Sencha Command`_ to build apps.  Please follow the instructions there to install
the tool.  Please make sure to use ExtJs_ version **6.x**.  On my machine, `sencha` gives me the following
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

	C:> virtualenv .
	C:> Scripts\activate
	C:> pip install -r requirements-windows.txt

ExtJS Framework Setup
~~~~~~~~~~~~~~~~~~~~~

Due to the size of the ExtJS_ framework, we don't include it in the repository.  Use `Sencha Command`_ to
create a initial empty app.  To do so. cd into the repo and::

	C:> sencha generate app -ext AppTemplate static

This will populate the `static/ext` directory with the needed framework files.


First Build
-----------

Always activate the virtualenv_!

Change directory to the repo dir and do::

	C:> Scripts\activate
	C:> npm install
	C:> grunt build


.. _Chokolatey: https://chocolatey.org/
.. _GOW: https://github.com/bmatzelle/gow/wiki
.. _virtualenv: https://virtualenv.pypa.io/en/latest/
.. _ExtJS: https://www.sencha.com/products/extjs/
.. _Node: https://nodejs.org/
.. _Sencha Command: https://www.sencha.com/products/extjs/#sencha-cmd
.. _Grunt: http://gruntjs.com/
.. _CoffeeScript: http://coffeescript.org/
.. _Fabric: http://www.fabfile.org/
.. _Sphinx: http://sphinx-doc.org/
.. _Python: http://www.python.org
.. _nexiles gateway: http://nexiles.com/products
.. _PTC Windchill: http://www.ptc-solutions.de/produkte/ptc-windchill/ptc-windchill-102.html
.. _us: mailto:info@nexiles.com?subject=nexiles.gateway%20apps%20request%20for%20information&cc=se@nexiles.de
.. _me: mailto:se@nexiles.com?subject=nexiles.gateway%20apps%20windows%20comments