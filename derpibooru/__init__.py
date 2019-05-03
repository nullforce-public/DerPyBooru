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

__title__ = "DerPyBooru"
__version__ = "0.9.0"
__author__ = "Joshua Stone"
__license__ = "Simplified BSD Licence"
__copyright__ = "Copyright (c) 2014-2018, Joshua Stone, Nullforce"

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
