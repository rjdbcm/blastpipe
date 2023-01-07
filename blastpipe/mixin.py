import abc
from typing import Any, Generic, TypeVar

# Abstract
class BaseMixin(abc.ABC):
    @abc.abstractclassmethod
    def extend_with(cls: Any, instance: Any) -> Any:
        """extend the instance with the mixin cls"""
        pass

# Generic
_T = TypeVar("_T", bound="BaseMixin")
class Mixin(Generic[_T], BaseMixin):...

# Helper Method
def mixin(cls: Any, base: Any) -> Any:
    def __wrapper(*args, **kwargs):
        return cls.extend_with(base(*args, **kwargs))
    return __wrapper