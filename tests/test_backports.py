import string

from hypothesis import given
from hypothesis import strategies as st

import lemprex.backports


@given(instance=st.builds(string.Template, st.text()))
def test_fuzz_TemplateGetIdentifiersMixin_extend_with(
    instance: string.Template,
) -> None:
    lemprex.backports.TemplateGetIdentifiersMixin.extend_with(instance=instance)
