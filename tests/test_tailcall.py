"""Tail call optimization tests"""
import pytest
from hypothesis import given
from hypothesis import strategies as st

import blastpipe.sequence
from blastpipe.sequence import chr_union


@given(active=st.booleans())
def test_fuzz_async_tail_call(active):
    """This test code was written by the `hypothesis.extra.ghostwriter` module"""
    blastpipe.sequence.async_tail_call(active=active)


def test_chr_union_range():
    """Test chr_union with a range"""
    assert chr_union((32, 35)) == {" ", "!", '"'}
    assert chr_union(32) == {" "}


@st.composite
def bad_input(draw):
    """Test bad input for chr_union"""
    return (
        draw(st.lists(st.floats())),
        draw(st.lists(st.text())),
        draw(st.lists(st.functions())),
        draw(st.lists(st.booleans())),
        draw(st.floats()),
        draw(st.text()),
        draw(st.functions()),
        draw(st.booleans()),
    )


@given(args=bad_input())
def test_fuzz_bad_input_chr_union(args):
    """Test bad input for chr_union"""
    with pytest.raises(TypeError):
        _ = chr_union(args)
