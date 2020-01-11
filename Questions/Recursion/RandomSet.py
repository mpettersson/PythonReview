"""
    RANDOM SET

    Write a method to randomly generate a set of m integers from an array of size n.  Each element must have equal
    probability of being chose.
"""
import random


def random_set_recursive(l, m, i=None):
    if i is None:
        i = len(l) - 1
    if i + 1 == m:
        return l[0:m]  # Return first m elements of original
    elif i + 1 > m:
        subset = random_set_recursive(l, m , i - 1)
        k = random.randint(0, i)
        if k < m:
            subset[k] = l[i]
        return subset
    return None


def random_set_iterative(l, m):
    subset = l[0:m]
    for i in range(m, len(l)):
        k = random.randint(0, i)
        if k < m:
            subset[k] = l[i]
    return subset


int_list = [x for x in range(0, 25)]
m = 5
print("m =", m)
print("int_list:", int_list, "\n")
print("random_set_recursive(int_list, m):", random_set_recursive(int_list, m))
print("random_set_iterative(int_list, m):", random_set_iterative(int_list, m))

