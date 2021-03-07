from math import sqrt

def hexagonal(n):
    if n == 0: return 0
    return 3 * n * (n - 1) + 1

def hexagonal_inverse(x):
    if x == 0: return 0
    return (3 + sqrt(12 * x - 3)) / 6