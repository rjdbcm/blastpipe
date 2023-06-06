"""BSD-3-Clause-Attribution Mixin ABC, Generic, and helper function.
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
from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar


# pylint: disable=too-few-public-methods
class BaseMixin(ABC):
    """Abstract mixin class"""

    @classmethod
    @abstractmethod
    def extend_with(cls: Any, instance: Any) -> Any:
        """extend the instance with the mixin cls"""


_T = TypeVar("_T", bound="BaseMixin")


class Mixin(Generic[_T], BaseMixin):
    """Generic mixin class"""


def mixin(cls: Any, base: Any) -> Any:
    """Helper function to extend the class with the base"""

    def __wrapper(*args, **kwargs):
        return cls.extend_with(base(*args, **kwargs))

    return __wrapper
