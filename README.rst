# Purpose

Template repository for python packages with continuous integration and delivery support. This will be used as the basis of my other python projects.

# setup

Asumptions:

* package sources are stored in `./src/%LibraryName%`
* tests are stored in `./test`
* we have a file `requirements.txt` to specify the dependencies of our package
* a configuration file `./src/%LibraryName%/metadata.py` that specify package metadata
* we have a `README.rst` file to describe the package