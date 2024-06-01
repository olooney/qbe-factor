QBE Factor Model
================

About
-----

Model inference endpoint for the QBE Factor model. 

Uses FastAPI and pydantic to define the JSON REST endpoint.

This project is an example/demo and not production quality.


Install
-------

Clone the git repo:

    git clone https://github.com/olooney/qbe-factor.git

This project provides a python package `qbe_factor`. Before installing it,
you should create an isolated environment, using conda or venv. For example:

    conda create -n qbe python=3.11.3
    conda activate qbe

For development, install `qbe_factor` in editable mode:

    pip install -e .[dev]

The `[dev]` will install additional dependencies needed only for development.
To install it normally, use:

    pip install .

The above will install the package with recent, up-to-date versions of all
dependences, which should work in most cases. However, if you are having
version compabability problems, you can run:

    pip install -r requirements.txt

to install all dependencies on the exact versions used for development.


Running the Server
------------------

To run the local test server, run:

    python scripts/run_server.py

This will start a local uvicorn instance serving on `localhost:8000` by
default; the port can be controlled by the PORT environment variable.

Visit `http://localhost:8000/ping` to check if the server has started
correctly.

Visit `http://localhost:8000/docs` for the interactive swagger docs.


Build and Test
--------------

In the root `qbe-factor` directory, run:
    
    pytest

To run the full suite of unit tests. Please do not submit a pull request
until all unit tests are passing.

Please also run:

    black .

To automatically force all `.py` files to adhere to the strict black style
guides.

How to Contribute
-----------------

Start from the main branch:

    git checkout main
    git pull

Create a feature branch:

    git checkout -b feature/feature-name

Make your changes as usual and push the branch to github:

    git push -u origin feature/feature-name

Then visit `https://github.com/olooney/qbe-factor` and create a pull request.


Sprint Backlog
--------------

[X] add model data
[X] model class
[X] test model
[X] unit tests
[ ] format / comments

[X] add API
[X] pydantic types
[ ] `var_name` validation
[ ] `category` validation
[X] unit tests
[ ] format / comments


Backlog
-------

[ ] Dockerfile?
[ ] Authentication?
[ ] DEV/PROD flags?
[ ] CLI?
