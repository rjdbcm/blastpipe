"""Utility functions for while loops"""
# pyright: reportGeneralTypeIssues=false
from contextlib import suppress
from typing import Any, Callable, Type, Tuple
__all__ = ('while_raised',)

def while_raised(exc_types: Tuple[Type[Exception]],
                 target: Callable,
                 *args,
                 implicit_break=True
    ) -> Any|None:
    """Repeats a target function while suppressing exceptions provided."""
    while True:
        with suppress(exc_types):
            if implicit_break:
                return target(*args)
            target(*args)
            break
