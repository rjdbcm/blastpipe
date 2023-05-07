"""Utility functions for tail call optimization."""
from typing import Annotated, Callable, Tuple, TypeAlias, Optional
import functools
TailCallFlag: TypeAlias = Tuple[()]
TailCallDecor: TypeAlias = Annotated[Optional[TailCallFlag], '@tail_call()']
TAIL_CALL: TailCallFlag = tuple() # PEP 484 Empty Tuple

DecoratedCallable: TypeAlias = Annotated[Callable, TailCallDecor]

def async_tail_call(active=True) -> DecoratedCallable:
    """Async tail_call decorator.
    Not deprecated as of Python 3.11
    """
    def __wrapper(func):
        async def _optimize_tuple(*args, **_):
            """Tail call optimization for tuple return."""
            while args.__class__ is tuple:  # Faster than isinstance()!
            #while isinstance(args, tuple):
                args = await func(*args)
            return args

        if active:
            functools.update_wrapper(_optimize_tuple, func)
            return _optimize_tuple

    return __wrapper
