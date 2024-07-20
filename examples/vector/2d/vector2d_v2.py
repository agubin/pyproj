from array import array
import math


class Vector2D:
    typrcode = 'd'

    @classmethod
    def frombytes(cls, octet):
        typecode = chr(octet[0])
        memv = memoryview(octet[1:]).cast(typecode)
        return cls(*memv)

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    """Give possibility to unpuck"""
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self) -> str:
        return str(tuple(self))
    
    def __bytes__(self) -> str:
        return (bytes(ord[self.typrcode]) + bytes(array(self.typrcode, self)))
    
    def __eq__(self, other) -> bool:
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self) -> bool:
        return bool(abs(self))
    
    def __format__(self, fmt: str = '') -> str:
        if fmt.endswith('p'):
            outer_format = '<{}, {}>'
            coords = (abs(self), self.angle())
            fmt = fmt[:-1]
        else:
            coords = self
            outer_format = '({}, {})'
        components = (format(c, fmt) for c in coords)
        return outer_format.format(*components)
    
    def angle(self):
        return math.atan2(self.x, self.y)
    

