import abc
import platform
import re
import string
from typing import List, Optional, Protocol, TypeVar

from .mixin import mixin, Mixin

PYMAJOR, PYMINOR, PYPATCH = map(int, platform.python_version_tuple())
__all__ = ('Template',)

class IsTemplatePre311(Protocol):
    delimiter: str
    # r'[a-z]' matches to non-ASCII letters when used with IGNORECASE, but
    # without the ASCII flag.  We can't add re.ASCII to flags because of
    # backward compatibility.  So we use the ?a local flag and [a-z] pattern.
    # See https://bugs.python.org/issue31672
    idpattern : r'str'
    braceidpattern: r'Optional[str]'
    flags: int
    pattern: re.Pattern
    template: str

    def safe_substitute(self): ...

    def substitute(self): ...



if PYMAJOR >= 3 and PYMINOR < 11:
    '''Here is a nice opportunity to show the preferred way of typing and using mixins'''
    T = TypeVar('T', bound='string.Template')

    class TemplateGetIdentifiersMixin(Mixin):
        
        delimiter: str
        idpattern : r'str'
        braceidpattern: r'Optional[str]'
        flags: int
        pattern: re.Pattern
        template: str

        def safe_substitute(self): ...

        def substitute(self): ...
        
        def get_identifiers(self: IsTemplatePre311) -> List[str]:
            ids = []
            for mo in self.pattern.finditer(self.template):
                named = mo.group('named') or mo.group('braced')
                if named is not None and named not in ids:
                    # add a named group only the first time it appears
                    ids.append(named)
                elif (named is None
                    and mo.group('invalid') is None
                    and mo.group('escaped') is None):
                    # If all the groups are None, there must beif PYMAJOR == 3 and PYMINOR < 11:

                    # another group we're not expecting
                    raise ValueError('Unrecognized named group in pattern',
                        self.pattern)
            return ids

        @classmethod
        def extend_with(cls: type[IsTemplatePre311], instance: T) -> T:

            instance.__class__ = type(
                f'{instance.__class__.__name__}With{cls.__name__}',
                (instance.__class__, cls),
                {},
            )
            return instance
    
    Template = mixin(TemplateGetIdentifiersMixin, string.Template)
else:
    Template = string.Template
