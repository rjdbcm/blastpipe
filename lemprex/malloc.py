"""Utilities for measuring memory usage.

Copyright 2012 Raymond Hettinger
Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom
the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from collections import deque
from itertools import chain
from sys import getsizeof, stderr

try:
    from reprlib import repr  # pylint: disable=redefined-builtin
except ImportError:  # pragma: defer to python
    pass


def total_size(obj, handlers=None, verbose=False):  # noqa: C901
    """Returns the approximate memory footprint an object and all of its contents.

    See `recipe <https://code.activestate.com/recipes/577504/>`__ for original.

    :param obj: object to measure size of
    :type  obj: object
    :param handlers: handlers to iterate over contents of containers, defaults to None
    :type  handlers: dict, optional
    :param verbose: whether to print verbose output, defaults to False
    :type  verbose: bool, optional
    :return: approximate memory footprint in bytes
    :rtype:  int

    Automatically finds the contents of the following builtin containers and
    their subclasses:  tuple, list, deque, dict, set and frozenset.
    To search other containers, add handlers to iterate over their contents:

        handlers = {SomeContainerClass: iter,
                    OtherContainerClass: OtherContainerClass.get_elements}
    """
    if handlers is None:
        handlers = {}

    def dict_handler(_dict):  # pragma: defer to python
        return chain.from_iterable(_dict.items())

    all_handlers = {
        tuple: iter,
        list: iter,
        deque: iter,
        dict: dict_handler,
        set: iter,
        frozenset: iter,
    }
    all_handlers.update(handlers)  # user handlers take precedence
    seen = set()  # track which object id's have already been seen
    default_size = getsizeof(0)  # estimate sizeof object without __sizeof__

    def sizeof(obj):
        if id(obj) in seen:  # pragma: defer to python
            return 0
        seen.add(id(obj))
        size_total = getsizeof(obj, default_size)

        if verbose:
            print(size_total, type(obj), repr(obj), file=stderr)

        for typ, handler in all_handlers.items():
            if isinstance(obj, typ):
                size_total += sum(map(sizeof, handler(obj)))
                break
        return size_total

    return sizeof(obj)
