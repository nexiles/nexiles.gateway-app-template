.. _maintainer_tasks:

Maintainer Tasks
================

Abstract
--------

Documentation for package maintainer related tasks.

Pushing Documentation to GitHub
-------------------------------

Source: http://daler.github.io/sphinxdoc-test/includeme.html

There's a fabric task::

	$ workon nexiles.gateway-app-template
	$ fab release_docs

You need to have the neccessary setup as detailled in the link above.  The gh-pages branch
is assumed to be checked out **next** to this repo, named `nexiles.gateway-app-template-docs`.