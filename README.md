# pydantic-compare-test

```
pydantic version:1.7.3
A symmetric pydantic BaseModel class comparison:  False
An asymmetric pydantic BaseModel class comparison:  False
A symmetric pydantic BaseModel object comparison with same class:  False
A symmetric pydantic BaseModel object comparison with different classes:  True
An asymmetric pydantic BaseModel object comparison with different classes:  False
A symmetric standard dataclasses class comparison:  False
Standard lib letting through custom type type-errors
Standard lib letting through custom type value-errors
Pydantic catching type errors on custom types
Pydantic letting through type errors, because it converted string '1' to 1 implicitly.

pydantic version:1.8.2
A symmetric pydantic BaseModel class comparison:  False
An asymmetric pydantic BaseModel class comparison:  False
A symmetric pydantic BaseModel object comparison with same class:  False
A symmetric pydantic BaseModel object comparison with different classes:  True
An asymmetric pydantic BaseModel object comparison with different classes:  False
A symmetric standard dataclasses class comparison:  False
Standard lib letting through custom type type-errors
Standard lib letting through custom type value-errors
Pydantic catching value errors on custom types
Pydantic letting through type errors, because it converted string '1' to 1 implicitly.

A final note, to use the json serializer function from pydantic but having validation on class level you can
refer directly to `from pydantic.json import pydantic_encoder`.

See:
https://pydantic-docs.helpmanual.io/usage/dataclasses/#json-dumping
https://www.python.org/dev/peps/pep-0557/#why-not-just-use-namedtuple
```
