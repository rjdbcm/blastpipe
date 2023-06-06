"""Mixin module tests."""
import typing

from hypothesis import given
from hypothesis import strategies as st

import lemprex.mixin


# pylint: disable=invalid-name
@given(instance=st.from_type(object))
def test_fuzz_BaseMixin_extend_with(instance: typing.Any) -> None:
    """This test code was written by the `hypothesis.extra.ghostwriter` module"""
    lemprex.mixin.BaseMixin.extend_with(instance=instance)


@given(cls=st.from_type(object), base=st.from_type(object))
def test_fuzz_mixin(cls: typing.Any, base: typing.Any) -> None:
    """This test code was written by the `hypothesis.extra.ghostwriter` module"""
    lemprex.mixin.mixin(cls=cls, base=base)
