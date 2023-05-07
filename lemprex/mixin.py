"""Mixin ABC, Generic, and helper function."""
from abc import abstractmethod, ABC
from typing import Any, Generic, TypeVar

#pylint: disable=too-few-public-methods
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
