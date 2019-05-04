# -*- coding: utf-8 -*-

"""
Derpibooru API bindings
~~~~~~~~~~~~~~~~~~~~~~~

Python bindings for Derpibooru's API

Typical usage:

>>> from derpibooru import Search, sort
>>> for image in Search().sort_by(sort.SCORE):
...   print(image.url)

Full API Documentation is found at <https://derpibooru.org/pages/api>.

Library documentation is found at <https://github.com/joshua-stone/DerPyBooru>.

"""
from os import path

# Get the version from the VERSION file
with open(path.join(path.abspath(path.dirname(__file__)), 'VERSION')) as version_file:
  version = version_file.read().strip()

__title__ = "DerPyBooru"
__version__ = version
__author__ = "Joshua Stone"
__license__ = "Simplified BSD Licence"
__copyright__ = "Copyright (c) 2014-2019, Joshua Stone, Nullforce"

from .search import Search
from .query import query
from .sort import sort
from .user import user

__all__ = [
  "Search",
  "query",
  "sort",
  "user"
]
