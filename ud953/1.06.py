# -*- coding: utf-8 -*-
# Lesson 1: Vectors
# Module 6: Quiz 2 (Magnitude, Direction)

from vector import Vector

# Problem 1 (length)
v = Vector([-0.221, 
             7.437])

print(v.length())

# Problem 2 (length)
v = Vector([ 8.813,
            -1.331,
            -6.247])

print(v.length())


# Problem 3 (normalize)
v = Vector([ 5.581,
            -2.136])

print(v.normalize())


# Problem 4 (normalize)
v = Vector([ 1.996,
             3.108,
            -4.554])

print(v.normalize())
