#!/usr/bin/env python3

compute_square = __import__('2-compute_square').compute_square

print(compute_square.__annotations__)
print(compute_square("meal", 3))
print(compute_square("college", 0.02))
