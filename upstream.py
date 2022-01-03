from pydantic import BaseModel

from dependency import B


class A(BaseModel):
    b: B


a = A(b=B(b=True))

# Try to use the dependency
try:
    assert a.b.a == a
except ValueError as err:
    assert str(err) == "Value not set. Please inject this property before calling."

# Inject the dependency
B.a = a

# Now we can use it
assert a.b.a == a

# Dependencies aren't serialized
assert a.dict() == {"b": {"b": True}}
