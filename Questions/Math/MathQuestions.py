"""
    CHECK FOR PRIMALITY

    Is a number prime?
"""
import math


# Check every num from 2 to math.sqrt(num) to see if it num % 2 is zero.
def is_prim(num):
    if num < 2:
        return False
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            return False
        i += 1
    return True


def is_prime_optimized(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i = i + 6
    return True


print("is_prim(0):", is_prim(0))
print("is_prim(-10):", is_prim(-10))
print("is_prim(2):", is_prim(2))
print("is_prim(100):", is_prim(100))
print("is_prim(113):", is_prim(113))


"""
    FACTORIAL
    
    Find the factorial of a number.
"""


def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


