"""Performance tests of microjet providers."""

import timeit


REPEAT = 3
NUMBER = 1000000


simple_object = timeit.Timer(
    setup="""
from microjet.ioc import Factory

class Obj(object):
    pass
    """,
    stmt="""
Obj()
    """)

simple_factory = timeit.Timer(
    setup="""
from microjet.ioc import Factory

class Obj(object):
    pass

object_factory = Factory(Obj)
    """,
    stmt="""
object_factory()
    """)

args_3_object = timeit.Timer(
    setup="""
from microjet.ioc import Factory

class Obj(object):
    def __init__(self, a, b, c):
        pass
    """,
    stmt="""
Obj(1, 2, 3)
    """)
args_3_factory = timeit.Timer(
    setup="""
from microjet.ioc import Factory

class Obj(object):
    def __init__(self, a, b, c):
        pass

object_factory = Factory(Obj, 1, 2, 3)
    """,
    stmt="""
object_factory()
    """)

kwargs_3_object = timeit.Timer(
    setup="""
from microjet.ioc import Factory

class Obj(object):
    def __init__(self, a, b, c):
        pass
    """,
    stmt="""
Obj(a=1, b=2, c=3)
    """)
kwargs_3_factory = timeit.Timer(
    setup="""
from microjet.ioc import Factory

class Obj(object):
    def __init__(self, a, b, c):
        pass

object_factory = Factory(Obj, a=1, b=2, c=3)
    """,
    stmt="""
object_factory()
    """)

print('Running tests:')
print('Simple object', simple_object.repeat(repeat=REPEAT, number=NUMBER))
print('Simple factory', simple_factory.repeat(repeat=REPEAT, number=NUMBER))

print('3 arguments', args_3_object.repeat(repeat=REPEAT, number=NUMBER))
print('3 arguments factory',
      args_3_factory.repeat(repeat=REPEAT, number=NUMBER))

print('3 keyword arguments',
      kwargs_3_object.repeat(repeat=REPEAT, number=NUMBER))
print('3 keyword arguments factory',
      kwargs_3_factory.repeat(repeat=REPEAT, number=NUMBER))
print('Done!')
