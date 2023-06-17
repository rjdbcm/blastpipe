"""Tests for backported code."""
import string

from hypothesis import given
from hypothesis import strategies as st

import blastpipe.backports


# pylint: disable=invalid-name
@given(instance=st.builds(string.Template, st.text()))
def test_fuzz_TemplateGetIdentifiersMixin_extend_with(instance: string.Template) -> None:
    """Test extension of arbitrary :py:class:`string.Template` text.

    :param instance: Text Template
    :type instance: string.Template
    """
    blastpipe.backports.TemplateGetIdentifiersMixin.extend_with(instance=instance)
