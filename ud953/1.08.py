# -*- coding: utf-8 -*-
# Lesson 1: Vectors
# Module 8: Quiz 3 (Dot Product, Angle)

from vector import Vector
from math import degrees

# Problem 1 (dot product)
v = Vector([ 7.887, 
             4.138])
w = Vector([-8.802, 
             6.776])

print(v.dot_product(w))


# Problem 2 (dot product)
v = Vector([-5.995,
            -4.904,
            -1.874])
w = Vector([-4.496,
            -8.755,
             7.103])

print(v.dot_product(w))


# Problem 3 (angle)
v = Vector([ 3.183,
            -7.627])
w = Vector([-2.668,
             5.319])

print(v.angle(w))

# Problem 4 (angle)
v = Vector([ 7.350,
             0.221,
             5.188])
w = Vector([ 2.751,
             8.259,
             3.985])

print(degrees(v.angle(w)))
