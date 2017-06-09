"""Performance tests of microjet providers."""

import timeit


REPEAT = 3
NUMBER = 1000000


args_5_object = timeit.Timer(
    setup="""
from microjet.ioc import Factory

class Obj(object):
    def __init__(self, a, b, c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

obj_factory = Factory(Obj)
    """,
    stmt="""
obj_factory(a=1, b=2, c=3, d=4, e=5)
    """)

args_6_object = timeit.Timer(
    setup="""
from microjet.ioc import Factory

class Obj(object):
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

delegate = Factory(object)
obj_factory = Factory(Obj, f=delegate.delegate())
    """,
    stmt="""
obj_factory(a=1, b=2, c=3, d=4, e=5)
    """)

args_6_object_stale = timeit.Timer(
    setup="""
from microjet.ioc import Factory

class Obj(object):
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

delegate = Factory(object)
obj_factory = Factory(Obj, a=1, b=2, c=3, d=4, e=5, f=delegate.delegate())
    """,
    stmt="""
obj_factory()
    """)

args_7_object = timeit.Timer(
    setup="""
from microjet.ioc import Factory

class Obj(object):
    def __init__(self, a, b, c, d, e, f, j):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.j = j

delegate = Factory(object)
obj_factory = Factory(Obj, f=delegate.delegate(), j=123)
    """,
    stmt="""
obj_factory(a=1, b=2, c=3, d=4, e=5)
    """)
print('Running tests:')

print('context-stale 5/0', args_5_object.repeat(repeat=REPEAT, number=NUMBER))
print('context-stale 6/1', args_6_object.repeat(repeat=REPEAT, number=NUMBER))
print('context-stale 6/6',
      args_6_object_stale.repeat(repeat=REPEAT, number=NUMBER))
print('context-stale 7/2', args_7_object.repeat(repeat=REPEAT, number=NUMBER))
