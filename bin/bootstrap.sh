#!/bin/bash
ROOT=$(dirname $0)/..
test -x "$ROOT/bin/python" || {
	echo "No virtual env -- creating ..."
	(
		cd $ROOT
		virtualenv .
		./bin/pip install -r requirements.txt --build-dir $ROOT/.pip_build
	)
}

source $ROOT/bin/activate
