# -*- coding: utf-8 -*-
# Lesson 1: Vectors
# Module 4: Quiz 1 (Plus, Minus, Scalar Multiply)

from vector import Vector

# Problem 1 (addition)
v = Vector([ 8.218, 
            -9.341])
w = Vector([-1.129,
             2.111])

print(v.plus(w))


# Problem 2 (subtraction)
v = Vector([ 7.119,
             8.215])
w = Vector([-8.223,
             0.878])

print(v.minus(w))


# Problem 3 (multiplication)
c = 7.41
v = Vector([ 1.671,
            -1.012,
            -0.318])

print(v.scale(c))
