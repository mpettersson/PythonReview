"""
    NUMBER SWAPPER

    Write a function to swap a number in place (that is, without temporary variable) (or a, b = b, a syntax).

    What it really means is, write a function, that takes two numbers and switches their values without using a
    temporary variable (or a, b = b, a syntax).
"""


def number_swapper(a, b):
    a = a - b
    b = a + b
    a = b - a
    return a, b


def bit_manipulation_number_swapper(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


a = 3
b = 5
print(f'a = {a}, b = {b}')
a, b = number_swapper(a, b)
print(f'a = {a}, b = {b}')
a, b = bit_manipulation_number_swapper(a, b)
print(f'a = {a}, b = {b}')


def make_dict(list_of_words):
    freq_dict = {}
    for w in list_of_words:
        c = w.strip().lower()
        if c in freq_dict:
            freq_dict[c] = freq_dict[c] + 1
        else:
            freq_dict[c] = 0
    return freq_dict



