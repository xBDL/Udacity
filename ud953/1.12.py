# -*- coding: utf-8 -*-
# Lesson 1: Vectors
# Module 12: Quiz 5 (Projection)

from vector import Vector

# Problem 1 (projection)
v = Vector([ 3.039, 
             1.879])
b = Vector([ 0.825, 
             2.036])

print(v.projection(b))


# Problem 2 (complement)
v = Vector([-9.880,
            -3.264, 
            -8.159])
b = Vector([-2.155, 
            -9.353,
            -9.473])

print(v.complement(b))


# Problem 3 (decomposition)
v = Vector([ 3.009,
            -6.172,
             3.692, 
            -2.510])
b = Vector([ 6.404, 
            -9.144,
             2.759,
             8.718])

print(v.projection(b))
print(v.complement(b))
