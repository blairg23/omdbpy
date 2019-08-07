import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="omdbpy",
    version="0.1.3",
    author="blairg23",
    author_email="blair@intelligen.technology",
    description="A minimalist Python wrapper for the Open Movie Database (OMDb) API (https://www.omdbapi.com/).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blairg23/omdbpy/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)