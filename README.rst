Purpose
=======

Template repository for python packages with continuous integration and delivery support. This will be used as the basis of my other python projects.

setup
=====

Asumptions:

* package sources are stored in `./src/%LibraryName%`
* tests are stored in `./test`
* we have a file `requirements.txt` to specify the dependencies of our package
* a configuration file `./src/%LibraryName%/metadata.py` that specify package metadata
* we have a `README.rst` file to describe the package


Builds
======

.. image:: https://dev.azure.com/civodlu/pte/_apis/build/status/civodlu.PythonTemplate?branchName=master
   :target: https://dev.azure.com/civodlu/pte/_build
   
.. image:: https://travis-ci.org/civodlu/PythonTemplate.svg?branch=master
	:target: https://travis-ci.org/civodlu/PythonTemplate/builds