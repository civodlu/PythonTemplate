Purpose
=======

Template repository for python packages with continuous integration and delivery support. This will be used as the basis of my other python projects.

Setup
=====

Asumptions:

* package sources are stored in `./src/%LibraryName%`
* tests are stored in `./test`
* we have a file `requirements.txt` to specify the dependencies of our package
* a configuration file `./src/%LibraryName%/metadata.py` that specify package metadata
* we have a `README.rst` file to describe the package

Stack
=====

* travis CI for continuous integration: register on https://travis-ci.org and activate the repository to activate in https://travis-ci.org/account/repositories and setup .travis.yml

* coveralls: register on https://coveralls.io and and update .travis.yml


How to use this template
========================

Add all the files to your project. The following files require customization:

* ./src/YourProjectName/metadata.py: important information regaring the project
* ./docs/source/conf.py: to be customized


TODO
====

* pre-commit: manages the git hooks. Must run `pre-commit install` with git in the path th first time. Run github desktop
from the activated conda env. Currently problems with "ERROR: Could not find a version that satisfies the requirement 
flake8 (from pre-commit-hooks==2.4.0) (from versions: none)"


Builds
======

.. image:: https://dev.azure.com/civodlu/pte/_apis/build/status/civodlu.PythonTemplate?branchName=master
	:target: https://dev.azure.com/civodlu/pte/_build
   
.. image:: https://travis-ci.org/civodlu/PythonTemplate.svg?branch=master
	:target: https://travis-ci.org/civodlu/PythonTemplate/builds
	
.. image:: https://coveralls.io/repos/github/civodlu/PythonTemplate/badge.svg?branch=master
	:target: https://coveralls.io/github/civodlu/PythonTemplate?branch=master
