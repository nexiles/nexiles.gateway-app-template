.. _introduction:

Introduction
============


What?
-----

This is a the nexiles app template which we use to develop apps for `PTC Windchill`_
using our `nexiles gateway`_ interface.

This template contains code and build scripts, and this documentation.

.. image:: images/screenshot.png

Features
--------

.. note:: These are features of the template project, not `nexiles gateway`_ features.

- Fully automated build
- Beautiful documentation
- Live reloading during development for instant feedback
- Hooks and examples for accessing `PTC Windchill`_ using `nexiles gateway`_

Why?
----

Usually, `PTC Windchill`_ extensions (or *customizations*) are coded in
Java, and the UI is done by customizing the `PTC Windchill`_ UI directly.

While this is fine for one-off projects, we find that the mainenance cost
of this approach is too high.

Using nexiles.gateway, we separate UI (front-end) from business logic (back-end),
and thus free ourselves (and the customer) from the restrictions and maintenance
overhead imposed by the normal customization approach.

Additionally, using nexiles.gateway allows us to use the dynamic programming language
Python_, which allows to use a more agile and interactive development process.  This
gives us and our customers a great advantage wrt. time-to-market and development costs,
as well as very quick iteration cycles.

For more information, contact us_.

Tools, Prerequisites
--------------------

This template application uses ExtJS_ for the UI, and the code is developed in CoffeeScript_.  The
documentation is written and published using Sphinx_.  The build automation uses Fabric_, a build tool
for Python_.

The CoffeeScript_ to JavaScript compiling, live reloading etc uses Grunt_.

To sum up, the prerequisites for building this project are:

- Node_
- Python_
- ExtJS_ -- the `ExtJS GPL version`_ is sufficient

And, if you want to actually test against `PTC Windchill`_:

- Access to `PTC Windchill`_ with installed `nexiles gateway`_.  You do **NOT** need
  file system or administrator rights.  A normal user account is enough.  You need to be
  able to create and iterate documents (`WTDocuments`).

  For more information, contact us_.

.. _ExtJS: https://www.sencha.com/products/extjs/
.. _ExtJS GPL version: https://www.sencha.com/legal/GPL/
.. _Grunt: http://gruntjs.com/
.. _Node: https://nodejs.org/
.. _CoffeeScript: http://coffeescript.org/
.. _Fabric: http://www.fabfile.org/
.. _Sphinx: http://sphinx-doc.org/
.. _Python: http://www.python.org
.. _nexiles gateway: http://nexiles.com/products
.. _PTC Windchill: http://www.ptc-solutions.de/produkte/ptc-windchill/ptc-windchill-102.html
.. _us: mailto:info@nexiles.com?subject=nexiles.gateway%20apps%20request%20for%20information&cc=se@nexiles.de