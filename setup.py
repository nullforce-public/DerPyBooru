#!/usr/bin/env python

from os import path
from setuptools import setup
from setuptools import find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(
  name = "DerPyBooru_Nullforce",
  # Versions should comply with PEP 440:
  # https://www.python.org/dev/peps/pep-0440/
  version = "0.9.0",
  description = "Python bindings for Derpibooru's API",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = "https://github.com/nullforce-forks/NF-DerPyBooru",
  author = "Nullforce",
  author_email = "glenngit@nullforce.com",
  license = "Simplified BSD License",
  platforms = ["any"],
  packages = find_packages(exclude=["tests"]),
  install_requires = ["requests"],
  include_package_data = True,
  #download_url = "https://github.com/joshua-stone/DerPyBooru/tarball/0.7.2",
  # For a list of valid classifiers, see https://pypi.org/classifiers/
  classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: BSD License",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3"
  ],
  keywords = "derpibooru ponies pony mlp"
)
