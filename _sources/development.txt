.. _development:

Development
===========

Abstract
--------

This chapter introduces and documents common developer tasks.

Please make sure that you set up your development environment correctly as detailled in :ref:`quickinstall_mac` or :ref:`quickinstall_win`.

Virtualenv
----------

All the shell commands listed here assume that you activated your virtualenv_.

Building the App
----------------

On a Mac, do::

	$ fab build

On Windows, do::

	C:> grunt build

Both commands will rebuild the App, which involves:

- Compiling CoffeeScript to JavaScript
- Regenerating the ExtJS Theme

Creating a *production* build
-----------------------------

On a Mac, the `build` task defaults to production mode::

	$ fab build

On Windows, do::

	C:> grunt coffee
	C:> cd static
	C:> sencha app build production

The minimized, compacted build will be placed in the `build` folder
in the `static` directory.


Serving the Web App locally for development
-------------------------------------------

On a Mac this will serve the development version and open a webbrowser
with the correct URL::

	$ fab serve

On Windows::

	C:> cd static
	C:> python -m SimpleHTTPServer

And open http://localhost:8000 in a web browser.

Developing and Live Reloading
-----------------------------

This setup needs two shells:

- One shell to watch for changes and compile&reload them
- One shell to serve the application

Watching (same for Mac and Windows)::

	grunt watch

For Serving (2nd shell), see above.

This will have Grunt_ watch for file changes in the source directory.  Grunt_ will
recompile changed files and reload them by *pushing* the changes directly to the browser
using web sockets.  For this to work, your browser needs to support web sockets.  We
use Google Chrome.

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