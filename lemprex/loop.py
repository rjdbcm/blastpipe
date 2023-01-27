
from contextlib import suppress
from typing import Any, Callable, Type, Tuple
__all__ = ('while_raised',)

def while_raised(exc_types: Tuple[Type[Exception]], target: Callable, *args, implicit_break=True) -> Any|None:
    while True:
        with suppress(exc_types):
            if implicit_break:
                return target(*args)
            target(*args)
            break
