"""
    OPERATIONS

    Write methods to implement the multiply, subtract, and divide operations for integers.  The result of all of these
    are integers.  Use ONLY the add operator.

    NOTE: Order of operations is key here!
"""


# To negate, you have to count down or up one at a time.
def negate(a):
    negated_a = 0
    new_sign = 1 if a < 0 else -1
    while a != 0:
        negated_a += new_sign
        a += new_sign
    return negated_a


def subtract(a, b):
    return a + (negate(b))


def multiply(a, b):
    c = 0
    if a == 0 or b == 0:
        return c
    if b < 0:
        a = negate(a)
        b = negate(b)
    while b != 0:
        c += a
        b += negate(1)
    return c


def divide(a, b):
    c = 0
    sign = 1
    if a == 0:
        return c
    if b == 0:
        raise ZeroDivisionError
    if a < 0:
        sign = negate(sign)
        a = negate(a)
    if b < 0:
        sign = negate(sign)
        b = negate(b)
    while a >= b and b > 0:
        c += 1
        b += negate(a)
    if sign < 0:
        c = negate(c)
    return c


print("negate(-5): ", negate(-5))
print("negate(0): ", negate(0))
print("negate(5): ", negate(5))

print("subtract(4, 5):", subtract(4, 5))
print("subtract(4, -5):", subtract(4, -5))
print("subtract(-4, 5):", subtract(-4, 5))
print("subtract(-4, -5):", subtract(-4, -5))
print("subtract(5, 5):", subtract(5, 5))
print("subtract(0, 5):", subtract(0, 5))
print("subtract(5, 0):", subtract(5, 0))
print("subtract(0, 0):", subtract(0, 0))

print("multiply(4, 5):  ", multiply(4, 5), "\t4 * 5:", 4*5)
print("multiply(4, -5): ", multiply(4, -5), "\t4 * -5:", 4*-5)
print("multiply(-4, 5): ", multiply(-4, 5), "\t-4 * 5:", -4*5)
print("multiply(-4, -5):", multiply(-4, -5), "\t-4 * -5:", -4*-5)
print("multiply(5, 5):  ", multiply(5, 5), "\t5 * 5:", 5*5)
print("multiply(0, 5):  ", multiply(0, 5), "\t0 * 5:", 0*5)
print("multiply(5, 0):  ", multiply(5, 0), "\t5 * 0:", 5*0)
print("multiply(0, 0):  ", multiply(0, 0), "\t0 * 0:", 0*0)

print("divide(4, 5):  ", divide(4, 5), "\t4 // 5:", 4 // 5)
print("divide(4, -5): ", divide(4, -5), "\t4 // -5:", 4 // -5)
print("divide(-4, 5): ", divide(-4, 5), "\t-4 // 5:", -4 // 5)
print("divide(-4, -5):", divide(-4, -5), "\t-4 // -5:", -4 // -5)
print("divide(5, 5):  ", divide(5, 5), "\t5 // 5:", 5 // 5)
print("divide(0, 5):  ", divide(0, 5), "\t0 // 5:", 0 // 5)
try:
    divide(5, 0)
except ZeroDivisionError:
    print("divide(5, 0): Raises ZeroDivisionError.")
try:
    divide(0, 0)
except ZeroDivisionError:
    print("divide(0, 0): Raises ZeroDivisionError.")

