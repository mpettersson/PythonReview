"""
    IS PRIME (CHECK FOR PRIMALITY)

    Is a number prime?

    Remember:
        A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
        A natural number greater than 1 that is NOT prime is called a composite number.
"""
import math


# Naive Solution: Check every num from 2 to num - 1 to see if it evenly divides the num.
def is_prime_naive(num):
    if num < 2:
        return False
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True


# Check every num from 2 to math.sqrt(num) to see if it num % i is zero.
def is_prime(num):
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


nums = [-10, 0, 1, 2, 3, 4, 100, 113]

[print(f"is_prime_naive({n}): {is_prime_naive(n)}") for n in nums]
print()

[print(f"is_prime({n}): {is_prime(n)}") for n in nums]
print()

[print(f"is_prime_optimized({n}): {is_prime_optimized(n)}") for n in nums]




