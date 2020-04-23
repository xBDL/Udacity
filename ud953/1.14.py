# -*- coding: utf-8 -*-
# Lesson 1: Vectors
# Module 14: Quiz 6 (Cross Product)

from vector import Vector

# Problem 1 (projection)
v = Vector([ 8.462,
             7.893, 
            -8.187])
w = Vector([ 6.984, 
            -5.975,
             4.778])

print(v.cross_product(w))


# Problem 2 (area of parallelogram)
v = Vector([-8.987,
            -9.838, 
             5.031])
w = Vector([-4.268, 
            -1.861,
            -8.866])

print(v.area_of_parallelogram(w))


# Problem 3 (area of triangle)
v = Vector([ 1.500,
             9.547, 
             3.691])
w = Vector([-6.007, 
             0.124,
             5.772])

print(v.area_of_triangle(w))
