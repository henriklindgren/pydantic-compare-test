from dataclasses import dataclass
from typing import List

from pydantic import BaseModel, version
import pydantic


class PydanticBasemodel1(BaseModel):
    a: int
    b: str


class PydanticBasemodel2(BaseModel):
    a: int
    b: str


class PydanticBasemodel3(BaseModel):
    a: str
    b: int


pydantic_basemodel_1 = PydanticBasemodel1(a=1, b='3')
pydantic_basemodel_2 = PydanticBasemodel1(a=2, b='4')
pydantic_basemodel_3 = PydanticBasemodel2(a=1, b='3')
pydantic_basemodel_4 = PydanticBasemodel3(a='5', b=4)


@dataclass
class StandardLibDataclass1(object):
    a: int
    b: str


@dataclass
class StandardLibDataclass2(object):
    a: int
    b: str


@dataclass
class StandardLibDataclass3(object):
    a: int
    b: str
    c: List[int]


@pydantic.dataclasses.dataclass
class PydanticDataclass1(object):
    a: int
    b: str
    c: List[int]


@dataclass
class StandardLibDataclass4(object):
    f: StandardLibDataclass3


class PydanticBasemodel4(BaseModel):
    f: StandardLibDataclass3


pydantic_cases = [
    ('A symmetric pydantic BaseModel class comparison: ', PydanticBasemodel1 == PydanticBasemodel2),
    ('An asymmetric pydantic BaseModel class comparison: ', PydanticBasemodel2 == PydanticBasemodel3),
    ('A symmetric pydantic BaseModel object comparison with same class: ', pydantic_basemodel_1 == pydantic_basemodel_2),
    ('A symmetric pydantic BaseModel object comparison with different classes: ', pydantic_basemodel_1 == pydantic_basemodel_3),
    ('An asymmetric pydantic BaseModel object comparison with different classes: ', pydantic_basemodel_1 == pydantic_basemodel_4),
]

standard_lib_cases = [
    ('A symmetric standard dataclasses class comparison: ', StandardLibDataclass1 == StandardLibDataclass2),
]


if __name__ == '__main__':
    print(f'pydantic version:{version.VERSION}')
    for message, result in pydantic_cases + standard_lib_cases:
        print(message, result)

    # MIXED CASES
    # A standard lib dataclass can't validate custom types
    wrong_value = StandardLibDataclass3(a=1, b='3', c=['1a', '2a'])
    wrong_type = StandardLibDataclass3(a=1, b='3', c=['1', '2'])
    right = StandardLibDataclass3(a=1, b='3', c=[1, 2])

    try:
        StandardLibDataclass4(f=wrong_type)
        print('Standard lib letting through custom type type-errors')
    except:  # noqa
        print('Standard lib catching type errors on custom types')

    try:
        StandardLibDataclass4(f=wrong_value)
        print('Standard lib letting through custom type value-errors')
    except:  # noqa
        print('Standard lib catching value errors on custom types')

    # But pydantic dataclasses extension can. Note nested models are upserted to pydantic support when the carrying
    # model is a BaseModel.
    try:
        PydanticBasemodel4(f=wrong_value)
        print('Pydantic letting through custom type value-errors')
    except pydantic.ValidationError:
        print('Pydantic catching value errors on custom types')

    try:
        PydanticBasemodel4(f=wrong_type)
        print("Pydantic letting through type errors, because it converted string '1' to 1 implicitly.")
    except pydantic.ValidationError:
        print('Pydantic catching type errors on custom types')
