from pydantic import BaseModel, version


class A(BaseModel):
    a: int
    b: str


class B(BaseModel):
    a: int
    b: str


class C(BaseModel):
    a: str
    b: int


a1 = A(a=1, b='3')
a2 = A(a=2, b='4')
b1 = B(a=1, b='3')
c1 = C(a='5', b=4)


if __name__ == '__main__':
    print(f'pydantic version:{version.VERSION}')
    print(
        ('A == B', A == B),
        ('B == C', B == C),
        ('a1 == a2', a1 == a2),
        ('a1 == b1', a1 == b1),
        ('a1 == c1', a1 == c1),
        ('b1 == c1', b1 == c1),
    )
