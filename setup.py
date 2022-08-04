import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="app_eng_hw",  
    version="0.0.1",
    author="Daniel Lizardo",  
    author_email="daniel@machinalabs.ai",  
    description="really just the readme and some assets for this",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # TODO: Change this to your repo URL
    url="https://github.com/Machina-Labs/python_template",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    # Pip-installable packages which are required for your
    # module to function are listed here
    install_requires=[
        'numpy',
    ],
    extras_require={
        # To install extra dependencies using the `pip install .[docs]` notation
        'docs': [
            'Sphinx',
            'sphinx-rtd-theme'
        ]
    },
    python_requires='>=3.6',
)
