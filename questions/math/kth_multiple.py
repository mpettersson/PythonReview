"""
    KTH MULTIPLE

    Design an algorithm to find the kth number such that the only prime factors are 3, 5, and 7.  Note that 3, 5, and 7
    do not have to be factors, but it should not hae any other prime factors.
    For example, the first several multiples would be (in order) 1, 3, 5, 7, 9, 15, 21.

    In other words, what is the kth smallest number in the form 3**A * 5**B * 7**C?

"""
import sys


# Approach 1: Brute Force, compute 3**A * 5**B * 7**C for all values of A, B, and C between 0 - k, put them in a list,
# sort the list, return the kth item; has a runtime of O(k**3 log k)...
def get_kth_multiple_brute_force(k):
    possibilities = all_possible_factors(k)
    possibilities.sort()
    return possibilities[k]


def all_possible_factors(k):
    values = []
    for a in range(k + 1):
        mult_three = 3**a
        for b in range(k + 1):
            mult_five = 5**b
            for c in range(k + 1):
                mult_seven = 7**c
                value = mult_three * mult_five * mult_seven
                values.append(value)
    return values


# Approach 2: Improved--Each time a new value, Vn, is added to the list, put Vn * 3, Vn * 5, and Vn * 7 into a queue and
# use the lowest value as Vn+1.
def get_kth_multiple_improved(k):
    if k < 0:
        return 0
    value = 1
    values = set()
    add_products(values, 1)
    for i in range(k):
        value = remove_min(values)
        add_products(values, value)
    return value


def add_products(values, value):
    for x in [3, 5, 7]:
        values.add(x * value)


def remove_min(values):
    min_value = None
    for v in values:
        if min_value is None or min_value > v:
            min_value = v
    values.remove(min_value)
    return min_value


# Approach 3: Optimal--Maintain three queues (one 3, 5, and 7)
def get_kth_multiple_optimal(k):
    if k < 0:
        return 0
    val = 0
    list3 = []
    list5 = []
    list7 = []
    list3.insert(0, 1)
    for i in range(k + 1):
        v3 = list3[0] if len(list3) > 0 else sys.maxsize
        v5 = list5[0] if len(list5) > 0 else sys.maxsize
        v7 = list7[0] if len(list7) > 0 else sys.maxsize
        val = min(v3, v5, v7)
        if val == v3:
            list3.pop(0)
            list3.append(3 * val)
            list5.append(5 * val)
        elif val == v5:
            list5.pop(0)
            list5.append(5 * val)
        elif val == v7:
            list7.pop(0)
        list7.append(7 * val)
    return val


sm_k = 5
lg_k = 100
print("sm_k = ", sm_k)
print("lg_k = ", lg_k)
print()

print("get_kth_multiple_brute_force(sm_k):", get_kth_multiple_brute_force(sm_k))
print("get_kth_multiple_brute_force(lg_k):", get_kth_multiple_brute_force(lg_k))
print()

print("get_kth_multiple_improved(sm_k):", get_kth_multiple_improved(sm_k))
print("get_kth_multiple_improved(lg_k):", get_kth_multiple_improved(lg_k))
print()

print("get_kth_multiple_optimal(sm_k):", get_kth_multiple_optimal(sm_k))
print("get_kth_multiple_optimal(lg_k):", get_kth_multiple_optimal(lg_k))
print()



