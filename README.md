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


Running the Local Server
------------------------

To run the local test server, run:

    python scripts/run_server.py

This will start a local uvicorn instance serving on `localhost:8000` by
default; the port can be controlled by the PORT environment variable.

Visit `http://localhost:8000/ping` to check if the server has started
correctly.

Visit `http://localhost:8000/docs` for the interactive swagger docs.


Building and Running in Docker
------------------------------

Ensure you have Docker installed, and in the root project directory run:

    docker build -t qbe/factor .

On my machine this builds a 232 MB image, which is fairly light.

You can run the image as a server with:

    docker run --rm -p 8000:8000 qbe/factor

You may also find it useful (for debugging) to run a shell inside the container:

    docker run --rm -it qbe/factor bash


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

1. [X] add model data
2. [X] model class
3. [X] test model
4. [X] unit tests
5. [X] format / comments

6. [X] add API
7. [X] pydantic types
8. [X] `var_name` validation
9. [X] `category` validation
10. [X] unit tests
11. [X] format / comments


Backlog
-------

1. [X] Dockerfile
2. [ ] Authentication?
3. [ ] DEV/PROD flags?
4. [ ] CLI?
5. [ ] Logging?
