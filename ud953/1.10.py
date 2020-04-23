# -*- coding: utf-8 -*-
# Lesson 1: Vectors
# Module 10: Quiz 4 (Parallel, Orthogonal)

from vector import Vector

# Problem 1 (parallel/orthogonal)
v = Vector([-7.579, 
            -7.880])
w = Vector([22.737, 
            23.640])

print(v.is_parallel(w))
print(v.is_orthogonal(w))


# Problem 2 (parallel/orthogonal)
v = Vector([-2.029,
             9.970, 
             4.172])
w = Vector([-9.231, 
            -6.639,
            -7.245])

print(v.is_parallel(w))
print(v.is_orthogonal(w))


# Problem 3 (parallel/orthogonal)
v = Vector([-2.328,
            -7.284, 
            -1.214])
w = Vector([-1.821, 
             1.072,
            -2.940])

print(v.is_parallel(w))
print(v.is_orthogonal(w))


# Problem 4 (parallel/orthogonal)
v = Vector([ 2.118, 
             4.827])
w = Vector([ 0.000, 
             0.000])

print(v.is_parallel(w))
print(v.is_orthogonal(w))
