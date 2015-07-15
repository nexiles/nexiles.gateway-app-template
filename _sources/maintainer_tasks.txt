.. _maintainer_tasks:

Maintainer Tasks
================

Abstract
--------

Documentation for package maintainer related tasks.

Pushing Documentation to GitHub
-------------------------------

Source: http://daler.github.io/sphinxdoc-test/includeme.html

You need to have the neccessary setup as detailled in the link above.  The gh-pages branch
is assumed to be checked out **next** to this repo, named `nexiles.gateway-app-template-docs`.

There's a fabric task for pushing everything to gh-pages.  This will **automatically** commit and
push, but **only the generated HTML on the gh-pages branch**::

	$ workon nexiles.gateway-app-template
	$ fab release_docs

Please make sure to check the docs using::

	$ workon nexiles.gateway-app-template
	$ fab docs

Look for warnings in the console, and visually check formatting.

Updating the Windchill App Template
-----------------------------------

To iterate (build, pack, upload) the Windchill app template which `nexiles.tools.api`_ uses
by default, do::

	$ workon nexiles.gateway-app-template
	$ fab build:which=windchill

This will:

- Perform a *production* build
- Assemble the built styles, ExtJS and Ext.ux to `static/build/windchill/AppTemplate`
- Create a `app-meta.json` using the current version
- Pack the app using `nxtools app pack`
- Upload the app using `nxtools app upload`

.. attention::  The app template uses a special `index.html` template which is
   copied from `static/index_windchill.html`


.. _nexiles.tools.api: http://nexiles.github.io/nexiles.tools.api