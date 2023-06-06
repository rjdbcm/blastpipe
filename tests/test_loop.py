"""Loop module tests."""
import typing

from hypothesis import given
from hypothesis import strategies as st

import lemprex.loop


@given(
    exc_types=st.tuples(st.just(Exception)),
    target=st.functions(),
    implicit_break=st.booleans(),
)
def test_fuzz_while_raised(
    exc_types: typing.Tuple[typing.Type[Exception]],
    target: typing.Callable,
    implicit_break,
) -> None:
    """This test code was written by the `hypothesis.extra.ghostwriter` module"""
    lemprex.loop.while_raised(
        exc_types=exc_types, target=target, implicit_break=implicit_break)
