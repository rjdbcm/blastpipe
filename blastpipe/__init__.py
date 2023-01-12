"""All boilerplate/gist/stackoverflow code for my projects goes here."""
from .backports import Template
from .context import maybeasynccontextmanager, MaybeAsyncGeneratorContextManager
from .mixin import Mixin, mixin
from .malloc import total_size
from .loop import while_raised
from .tailcall import async_tail_call
from .sequence import chr_union
from ._static_version import version

__version__ = version

__all__ = (
    'chr_union',
    'maybeasynccontextmanager', 
    'MaybeAsyncGeneratorContextManager',
    'Template',
    'Mixin',
    'mixin',
    'total_size',
    'while_raised',
    'async_tail_call',
    '__version__'
)
