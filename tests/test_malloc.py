"""Malloc module tests."""
from typing import Tuple

from hypothesis import given
from hypothesis import strategies as st

import lemprex.malloc


@st.composite
def sized_objects(draw) -> Tuple[st.SearchStrategy, ...]:
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


@given(obj=sized_objects(), verbose=st.booleans())
def test_fuzz_total_size(obj, verbose):
    """This test code was written by the `hypothesis.extra.ghostwriter` module"""
    lemprex.malloc.total_size(obj=obj, handlers=None, verbose=verbose)
