"""
    PHONE KEYPAD NUM TO LETTER COMBINATIONS (leetcode.com/problems/letter-combinations-of-a-phone-number)

    Write a function, which when given a string s containing digits from 2-9 (inclusive), return all possible letter
    combinations that the number could represent if any number of the individual digits were pressed (order of the
    result doesn't matter).

    The mapping of digit to letters is:
                            2: a, b, c      3: d, e, f
            4: g, h, i      5: j, k, l      6: m, n, o
            7: p, q, r, s   8: t, u, v      9: w, x, y, z

    Example:
        Input = '23'
        Output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""
import itertools


# APPROACH: Recursion
#
# Recurse over the digit string starting at index zero.  If the index is equal to the digit strings length then return
# an empty list, if the index is equal to one less than the digit strings length, return the mapped values, else return
# a list consisting of each of the mapped values concatenated with each of the results of a recursive call with the next
# index.
#
# Time Complexity: O(n), where n is the length of s.
# Space Complexity: O(4**n), where n is the length of s.
def phone_keypad_num_to_letter_combinations_rec(s):

    def _rec(s, i):
        d = {'2': ['a', 'b', 'c'],      '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],      '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        if i == len(s):
            return []
        if i == len(s) - 1:
            return d[s[i]]
        return [c + res for c in d[s[i]] for res in _rec(s, i+1)]

    if isinstance(s, str):
        return _rec(s, 0)


# APPROACH: Iterative
#
# Simply iterate over the digits characters, if it is the first character return it's mapping, else, make a new list
# with the product of the previous characters results and current characters mapped values.
#
# Time Complexity: O(n), where n is the length of s.
# Space Complexity: O(4**n), where n is the length of s.
def phone_keypad_num_to_letter_combinations(s):
    if isinstance(s, str):
        d = {'2': ['a', 'b', 'c'],      '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],      '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        result = []
        for i, n in enumerate(s):
            if i == 0:
                result = d[n]
            else:
                result = [e + v for e in result for v in d[n]]
        return result


# APPROACH: Via Itertools Product
#
# This two-liner uses itertools' product function.
#
# Time Complexity: O(n), where n is the length of s.
# Space Complexity: O(4**n), where n is the length of s.
def phone_keypad_num_to_letter_combinations_min(s):
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    return list(map(''.join, itertools.product(*map(mapping.__getitem__, s)))) if s else ''


args = ['23',
        '2',
        '7',
        '',
        '2222',
        '69',
        '42',
        None]
fns = [phone_keypad_num_to_letter_combinations_rec,
       phone_keypad_num_to_letter_combinations,
       phone_keypad_num_to_letter_combinations_min]

for s in args:
    print(f"digits string s: {s!r}")
    for fn in fns:
        print(f"{fn.__name__}(s): {fn(s)}")
    print()


