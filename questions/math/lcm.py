"""
    LEAST COMMON MULTIPLE (LCM)

    In arithmetic and number theory, the least common multiple, lowest common multiple, or smallest common multiple of
    two integers a and b, is the smallest positive integer that is divisible by both a and b.

    Since division of integers by zero is undefined, this definition has meaning only if a and b are non-zero. However,
    some authors define lcm(a,0) as 0 for all a, which is the result of taking the lcm to be the least upper bound in
    the lattice of divisibility.

    SEE: https://en.wikipedia.org/wiki/Least_common_multiple for more information.
"""


# GCD Approach:
def lcm(a, b):
    if a or b:
        return abs(a * b)/gcd(a, b)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


# TODO Prime Factorization Approach:
def lcm_prime_fact(a, b):
    pass


args = [(200, 310), (10, 275), (468, 279), (120, 390), (480, 430), (33, 69), (-150, 348), (-462, -264), (465, -18),
        (10, 0), (0, 10), (0, 0)]

for a, b in args:
    print(f"lcm({a}, {b}): {lcm(a, b)}")
print()


