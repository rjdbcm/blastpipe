"""BSD-3-Clause-Attribution Backports starting from Python 3.9
Copyright (c) 2023 Ross J. Duff MSc
Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.
    2. Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.
    3. Neither the name of the copyright holder nor the names of its contributors
    may be used to endorse or promote products derived from this software without
    specific prior written permission.
    4. Redistributions of any form whatsoever must retain the following acknowledgment:
    'This product includes software developed by the
    Peculiar Software Company LLC (http://www.github.com/rjdbcm/).'

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import platform
import re
import string
from datetime import date
from typing import List, Optional, Protocol, TypeVar

from .mixin import Mixin, mixin

PYMAJOR, PYMINOR, PYPATCH = map(int, platform.python_version_tuple())

minor_deprecation = {
    9: date(2025, 10, 1),
    10: date(2026, 10, 1),
    11: date(2027, 10, 1),
}


# pylint: disable=missing-function-docstring
class IsTemplatePre311(Protocol):
    """Protocol to check if a Template is pre-3.11"""

    delimiter: str
    # r'[a-z]' matches to non-ASCII letters when used with IGNORECASE, but
    # without the ASCII flag.  We can't add re.ASCII to flags because of
    # backward compatibility.  So we use the ?a local flag and [a-z] pattern.
    # See https://bugs.python.org/issue31672
    idpattern: r"str"
    braceidpattern: r"Optional[str]"
    flags: int
    pattern: re.Pattern
    template: str

    def safe_substitute(self):
        ...

    def substitute(self):
        ...


T = TypeVar("T", bound="string.Template")


class TemplateGetIdentifiersMixin(Mixin):
    """Example Template mixin with preferred way of typing and using mixins"""

    delimiter: str
    idpattern: r"str"
    braceidpattern: r"Optional[str]"
    flags: int
    pattern: re.Pattern
    template: str

    def safe_substitute(self):
        """Abstract method to be implemented by base"""

    def substitute(self):
        """Abstract method to be implemented by base"""

    def get_identifiers(self: IsTemplatePre311) -> List[str]:  # pragma: defer to string
        """Mixin method get_identifiers for older Template pre-3.11"""
        ids = []
        for i in self.pattern.finditer(self.template):
            named = i.group("named") or i.group("braced")
            if named is not None and named not in ids:
                # add a named group only the first time it appears
                ids.append(named)
            elif named is None and i.group("invalid") is None and i.group("escaped") is None:
                # If all the groups are None, there must be
                # another group we're not expecting
                raise ValueError("Unrecognized named group in pattern", self.pattern)
        return ids

    @classmethod
    def extend_with(cls: type[IsTemplatePre311], instance: T) -> T:
        instance.__class__ = type(
            f"{instance.__class__.__name__}With{cls.__name__}",
            (instance.__class__, cls),
            {},
        )
        return instance


if PYMAJOR >= 3 and PYMINOR < 11:
    Template = mixin(TemplateGetIdentifiersMixin, string.Template)  # pragma: defer to string
else:
    Template = string.Template  # pragma: defer to string
