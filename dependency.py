from typing import TYPE_CHECKING, Type, ClassVar

from pydantic import BaseModel, Field


if TYPE_CHECKING:
    from upstream import A

class dependency(property):
    """
    Dependencies are injected class variables that must be set before use
    NOTE: do not appear in a Pydantic model's set of properties
    """

    def __get__(self, *args):
        raise ValueError("Value not set. Please inject this property before calling.")

class B(BaseModel):
    a: ClassVar["A"] = dependency()
    b: bool = False
