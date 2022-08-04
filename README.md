# python_template

A template repository for making an installable Python module. Make sure to
find the `#TODO`s to rename appropriate strings to customize this template for
your module.

## Setup

### Local Development

To install `python_template` for onto your machine for local testing and development:

```
git clone https://github.com/Machina-Labs/python_template.git
cd /local/path/to/python_template
pip install -e .
```

This will be installed globally to whatever environment you have active.

To install the optional dependencies to build the documentation, run:

`pip install -e .[docs]`

### Module Dependency

If your repository has a `setup.py` file, make sure to add `python_template` as a dependency:

```
setuptools.setup(
	install_requires=[
		"python_template @ git+https://github.com/Machina-Labs/python_template",
	],
)
```

# Build the Docs

To build the documentation, navigate to the docs directory and run:

```
cd docs
make html
```

If the source code has changed, to re-build the .rst files, run:

```
cd docs/source
sphinx-apidoc -o ./ ../../python_template
cd ..
make html
```

# Run the tests

To run a test suite, run:

`python -um tests.test_some_module.py`
