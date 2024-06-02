QBE Factor Model
================

About
-----

Model inference endpoint for the QBE Factor model. This model computes risk
adjustment factors for demographic cohorts.

It uses FastAPI and pydantic to define JSON REST API. The key endpoint is
`/get_factors` which accepts a list of variables (`var_name`/`category` pairs)
as JSON and returns a similar JSON data structure with the numeric `factor`
added to each variable.

This project is an example/demo and not production quality.


Design Notes
------------

This project was designed to eventually support several modes of inference; the
REST API endpoint for real-time inference is a good place to start, but most
projects will eventually need bulk inference, a command-line-interface, or even
a direct Python API integration. To support these use cases, we follow the
Model/View seperation pattern, where as much logic as possible in implemented
in `qbe_factor.models` where it can be shared across inferfaces, and only logic
specific to the real-time REST endpoint is is included in `qbe_factor.api`.

Next, It wasn't clear how dynamic and "data-driven" the endpoint is supposed to
be so we've assumed - for the time being - that the set of `var_name` and
`category` values are fairly static while the actual numeric factors change
fairly often. As such, we've hard coded that information into the types of the
Enums and pydantic classes used for validation. If the intention is to have a
generic, data-driven "engine" that can support arbitary `var_name` and
`category` values just by supplying a new `data.json` file, the project can be
refactored to support that.

Finally, a production-grade API would probably has support for authentication,
loggging, configurable DEV/PROD behavior, and so on. As these "non-fuctional
requirments" depend on the details of the deployment environment they've all
been omitted for now.

See the "Backlog" below for a list of suggested future enhancements.


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

Finally, the build the wheel for the package, run:

    python setup.py bdist_wheel

This will create a `.whl` file in the `dist` directory, which you can then
distribute as you see fit.


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

If the build was successful, you can run the image as a server with:

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
4. [ ] Bulk Inference?
5. [ ] CLI?
6. [ ] Logging?

