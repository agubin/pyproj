import typing


Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('lon', float)])
# Another way
# Coordinate = typing.NamedTuple('Coordinate', lat=float, lon=float)

# And one more
# class Coordinate(typing.NamedTuple):
#     lat: float
#     lon: float

#     def __str__(self):
#         return 'Some realization for Coordinate'

# moscow = Coordinate(55.317, 54.874)
# typing.get_type_hints(moscow)
# typing.get_type_hints(Coordinate)

class DemoNT(typing.NamedTuple):
    a: int
    b: int
    c: str = 'some'
    d = 'spam'