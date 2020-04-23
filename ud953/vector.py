from decimal import Decimal, getcontext
from math import acos, sqrt

getcontext().prec = 30

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    # Quiz1 (Plus, Minus, Scalar Multiply)
    def plus(self, v):
        return Vector([x + y for x,y in zip(self.coordinates,v.coordinates)])

    def minus(self, v):
        return Vector([x - y for x,y in zip(self.coordinates,v.coordinates)])

    def scale(self, c):
        return Vector([Decimal(c) * x for x in self.coordinates])

    # Quiz2 (Magnitude, Direction)
    def length(self):
        return Decimal(sqrt(sum([x**2 for x in self.coordinates])))
    
    def normalize(self):
        length = self.length()
        if length == 0:
            print("Zero vector has no lengthalization")
        else:
            return self.scale(Decimal(1.0)/length)

    # Quiz3 (Dot Product, Angle)
    def dot_product(self, v):
        return sum([x * y for x,y in zip(self.coordinates,v.coordinates)])

    def angle(self, v):
        vunit = v.normalize()
        return acos(vunit.dot_product(self.normalize()))
    
    # Quiz4 (Parallel, Orthogonal)
    def is_parallel(self, v, tol=1e-9):
        if self.length() < tol or v.length() < tol:
            return True
        else:
            vunit = v.normalize()
            return 0 < tol - abs(1 - abs(vunit.dot_product(self.normalize())))
    
    def is_orthogonal(self, v, tol=1e-9):
        return 0 < tol - abs(self.dot_product(v))

    # Quiz5 (Projection)
    def projection(self, b):
        if b.length() == 0:
            print("Cannot project onto zero vector")
        else:
            bunit = b.normalize()
            return bunit.scale(self.dot_product(bunit))
    
    def complement(self, b):
        return self.minus(self.projection(b))
    
    # Quiz6 (Cross Product)
    def cross_product(self, v):
        a1, a2, a3 = self.coordinates
        b1, b2, b3 = v.coordinates
        return Vector([a2 * b3 - a3 * b2,
                       a3 * b1 - a1 * b3,
                       a1 * b2 - a2 * b1])
    
    def area_of_parallelogram(self, v):
        cross = self.cross_product(v)
        return cross.length()
    
    def area_of_triangle(self, v):
        return Decimal(0.5) * self.area_of_parallelogram(v)
    