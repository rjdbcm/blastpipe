"""Mixin module tests."""
import typing

from hypothesis import given
from hypothesis import strategies as st

import blastpipe.mixin
import blastpipe.malloc
import blastpipe.loop


@st.composite
def sized_objects(draw) -> typing.Tuple[st.SearchStrategy, ...]:
    """sized object strategy"""
    return (
        draw(st.binary()),
        draw(st.booleans()),
        draw(st.complex_numbers()),
        draw(st.datetimes()),
        draw(st.floats()),
        draw(st.integers()),
        draw(st.text()),
        draw(st.timedeltas()),
        draw(st.timezone_keys()),
        draw(st.times()),
        draw(st.uuids()),
    )


# pylint: disable=invalid-name
@given(instance=st.from_type(object))
def test_fuzz_BaseMixin_extend_with(instance: typing.Any) -> None:
    """This test code was written by the `hypothesis.extra.ghostwriter` module"""
    blastpipe.mixin.BaseMixin.extend_with(instance=instance)  # type: ignore


@given(cls=st.from_type(object), base=st.from_type(object))
def test_fuzz_mixin(cls: typing.Any, base: typing.Any) -> None:
    """This test code was written by the `hypothesis.extra.ghostwriter` module"""
    blastpipe.mixin.mixin(cls=cls, base=base)


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
    blastpipe.loop.while_raised(
        exc_types=exc_types, target=target, implicit_break=implicit_break
    )


@given(obj=sized_objects(), verbose=st.booleans())
def test_fuzz_total_size(obj, verbose):
    """This test code was written by the `hypothesis.extra.ghostwriter` module"""
    blastpipe.malloc.total_size(obj=obj, handlers=None, verbose=verbose)
