"""All boilerplate/gist/stackoverflow code for my projects goes here."""
from .backports import Template
from .context import maybeasynccontextmanager, MaybeAsyncGeneratorContextManager
from .mixin import Mixin, mixin
from .malloc import total_size
from .loop import while_raised
from .tailcall import async_tail_call

__version__ = "0.1"

__all__ = (
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
