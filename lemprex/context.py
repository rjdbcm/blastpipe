# pylint: disable=invalid-name
from contextlib import contextmanager, asynccontextmanager
from functools import wraps

class MaybeAsyncGeneratorContextManager:
    """Decorate a generator for use as both a context manager and as an async context manager.
    Not deprecated as of Python 3.11.1
    https://stackoverflow.com/a/61977720
    credit: Andy Jones

    """
    def __init__(self, func, args, kwargs):
        self._func = func
        self._args = args
        self._kwargs = kwargs
        self._sync = None
        self._async = None

    def __enter__(self):
        if self._sync is None:
            syncfunc = contextmanager(self._func)
            self._sync = syncfunc(*self._args, **self._kwargs) # type: ignore
        return type(self._sync).__enter__(self._sync)

    def __exit__(self, t, v, tb):
        return type(self._sync).__exit__(self._sync, t, v, tb) # type: ignore
    def __aenter__(self):
        if self._async is None:
            @asynccontextmanager
            async def asyncfunc(*args, **kwargs):
                with contextmanager(self._func)(*args, **kwargs): # type: ignore
                    yield 
            self._async = asyncfunc(*self._args, **self._kwargs)
        return type(self._async).__aenter__(self._async)

    def __aexit__(self, t, v, tb):
        return type(self._async).__aexit__(self._async, t, v, tb) # type: ignore

def maybeasynccontextmanager(func):
    """convenience wrapper for monadic context managers"""
    @wraps(func)
    def helper(*args, **kwds):
        return MaybeAsyncGeneratorContextManager(func, args, kwds)
    return helper
