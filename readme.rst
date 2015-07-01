nexiles gateway app template
============================

This repository contains template code for nexiles gateway apps.

Tools
-----

- Fabric for packaging and automation
- Sphinx for documentation
- ExtJS for UI
- coffee script for UI logic
- grunt for building

Quick setup
-----------

::

	cd develop/nexiles
	git clone git@github.com:nexiles/nexiles.gateway-app-template.git
	cd nexiles.gateway-app-template
	virtualenv .
	. ./bin/activate
	pip install -r requirements
	fab full_monty

Repo Layout
-----------

::
	.
	├── docs
	├── src
	│   └── AppTemplate
	│       └── app
	│           ├── model
	│           ├── store
	│           ├── view
	│           │   └── main
	│           └── widgets
	└── static
	    ├── app
	    ├── app.json
	    ├── build
	    ├── ext
	    ├── overrides
	    ├── packages
	    ├── resources
	    └── sass

**docs**
	Sphinx documentation

**src**
	CoffeeScript sources for the application

**static/app**
	Built JavaScript

**static/app.json**
	ExtJS app specific configuration

**static/sass**
	ExtJS app styling

**static/{ext,overrides,packages,build}**
	ExtJS managed