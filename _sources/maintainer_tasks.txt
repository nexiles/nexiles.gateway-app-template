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
