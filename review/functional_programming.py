"""

    SEE:
        https://www.burgaud.com/foldl-foldr-python
        https://stackoverflow.com/questions/10366374/what-is-the-pythonic-equivalent-to-the-fold-function-from-functional-program
"""
import functools
import operator


# FOLDS
# In functional programming, fold (also termed reduce, accumulate, aggregate, compress, or inject) refers to a family of
# higher-order functions that analyze a recursive data structure and through use of a given combining operation,
# recombine the results of recursively processing its constituent parts, building up a return value.
#
# Fold arguments are:
#     f:    The function (or, combining operation) to apply.
#     l:    The list to fold; A.K.A. [h:t] or [x:xs].
#     b:    The base case, or the accumulator value; A.K.A. a or z.


# FOLD LEFT (AKA functools.reduce)
# Is left associative.
#
# Visually, foldl(f, [1, 2, 3, 4], b), would resemble:
#
#                f
#              /   \
#             f     4
#           /   \
#          f     3
#        /   \
#       f     2
#     /   \
#    b     1
#
# Or, given f is operator.sub (-) and b is 0:
#   operator.sub(operator.sub(operator.sub(operator.sub(0, 1), 2), 3), 4)
# Which, is equivalent to: (((0 - 1) - 2) - 3) - 4) == -10


# Fold Left Function:
def foldl(f, l, b):
    return b if len(l) == 0 else foldl(f, l[1:], f(b, l[0]))


# OR, using functools.reduce:
def fold_l(f, l, b):
    return functools.reduce(f, l, b)
# OR, just use inline:
# functools.reduce(f, l, b)


# Fold Left Lambda:
fold_l_lambda = lambda f, l, b: b if len(l) == 0 else fold_l_lambda(f, l[1:], f(b, l[0]))


# FOLD RIGHT
# Is right associative.
#
# Visually, foldr(f, [1, 2, 3, 4], b), would resemble:
#
#       f
#     /   \
#    1     f
#        /   \
#       2     f
#           /   \
#          3     f
#              /   \
#             4     b
#
# Or, given f is operator.sub (-) and b is 0:
#   operator.sub(1, operator.sub(2, operator.sub(3, operator.sub(4, 0))))
# Which, is equivalent to: (1 - (2 - (3 - (4 - 0))) == -2


# Fold Right Function:
def foldr(f, l, b):
    return b if len(l) == 0 else f(l[0], foldr(f, l[1:], b))


# OR, using functools.reduce:
def fold_r(f, l, b):
    return functools.reduce(lambda x, y: f(y, x), reversed(l), b)
# OR, just use inline:
# functools.reduce(lambda x, y: f(y, x), reversed(l), b)


# Fold Right Lambda
foldr_lambda = lambda f, l, b: b if len(l) == 0 else f(l[0], foldr(f, l[1:], b))


# NOTE:
def flip(func):
    @functools.wraps(func)
    def newfunc(x, y):
        return func(y, x)
    return newfunc


num_l = list(range(1,2))

print("Sum (ftools):", functools.reduce(lambda x, y: x + y, num_l, 0))
print("Sum (foldl): ", foldl(lambda x, y: x + y, num_l, 0))
print("Sum (foldr): ", foldr(lambda x, y: x + y, num_l, 0))
print()

print("Sub (ftools):", functools.reduce(lambda x, y: x - y, num_l, 0))
print("Sub (foldl): ", foldl(lambda x, y: x - y, num_l, 0))
print("Sub (foldr): ", foldr(lambda x, y: x - y, num_l, 0))
print()

print("Mlt (ftools):", functools.reduce(lambda x, y: x * y, num_l, 10))
print("Mlt (foldl): ", foldl(lambda x, y: x * y, num_l, 10))
print("Mlt (foldr): ", foldr(lambda x, y: x * y, num_l, 10))
print()

print("Div (ftools):", functools.reduce(lambda x, y: x / y, num_l, 10))
print("Div (foldl): ", foldl(lambda x, y: x / y, num_l, 10))
print("Div (foldr): ", foldr(lambda x, y: x / y, num_l, 10))
print()

print("Any (ftools):", functools.reduce(lambda x, y: x or y, [False, True, False], False))
print("Any (foldl): ", foldl(lambda x, y: x or y, [False, True, False], False))
print("Any (foldr): ", foldr(lambda x, y: x or y, [False, True, False], False))
print()

print("All (ftools):", functools.reduce(lambda x, y: x and y, [False, True, False], True))
print("All (foldl): ", foldl(lambda x, y: x and y, [False, True, False], True))
print("All (foldr): ", foldr(lambda x, y: x and y, [False, True, False], True))
print()


# TODO ADD CURRIED VERSIONS
# Fold Right Function:
# def foldr(f):
#     def accumulator(a):
#         def list_func(l):
#             if l:
#                 h = l[0]
#                 t = l[1:]
#                 return f(h)(foldr(f)(a)(t))
#             else:
#                 return a
#         return list_func
#     return accumulator


def curried_add(x):
    def inner(y):
        return x + y
    return inner


def curried_mult(x):
    def inner(y):
        return x * y
    return inner


# print(foldr(curried_add)(0)([1, 2, 3, 4, 5]))
# print(foldr(curried_mult)(1)([1, 2, 3, 4, 5]))


# Y COMBINATOR
# In functional programming, the Y combinator can be used to formally define recursive functions in a programming
# language that does not support recursion.
# SEE: https://en.wikipedia.org/wiki/Fixed-point_combinator#Y_combinator

lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))

# SEE https://stackoverflow.com/questions/13591970/does-python-optimize-tail-recursion for more.


