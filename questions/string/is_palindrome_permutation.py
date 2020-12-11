"""
    IS PALINDROME PERMUTATION (CCI 1.4: PALINDROME PERMUTATION
                               EPI 13.1: TEST FOR PALINDROMIC PERMUTATIONS)

    Write a function that accepts a string and returns True if the string is a permutation of a palindrome, False
    otherwise.  Where a palindrome is a sequence of one or more characters, that may or may not contain dictionary
    words, which reads the same backward as forward.

    Example:
        Input = "Tact Coa"
        Output = True (permutations: "taco cat", "atco cta", etc.)
"""
import itertools
import re


# Questions to ask the interviewer:
#   - What type of text; ASCII, Unicode, etc.?
#   - Spaces?
#   - Capitalization?


# Naive/Brute Force Approach:  Generate permutations of the string, if one is a palindrome return True, else when no
# more permutations exists, return False.
# Time Complexity: O(n!), where n is the length of the string.
# Space Complexity: O(n), where n is the length of the string, IFF itertools.permutations is O(n).
def is_palindrome_permutation_naive(string):

    def _is_palindrome(l):
        lo = 0
        hi = len(l) - 1
        while lo <= hi:
            if l[lo] != l[hi]:
                return False
            lo += 1
            hi -= 1
        return True

    if string:
        for permutation in itertools.permutations(string.lower()):
            if _is_palindrome(permutation):
                return True
    return False


# Dictionary/Hash Map Approach:  Using a dictionary to store the multiplicity of each letter in the string.  If the
# string is an odd length then at most there can be one char with an odd number, if the string is an even length then
# all chars must be a multiple of two for the string to be a palindrome.
# Time Complexity: O(n), where n is the number of characters in the string.
# Space Complexity: O(u), where u are the number of unique characters in the string.
def is_palindrome_permutation(string):
    if string and len(string) > 0:
        d = dict()
        num_odd = 0
        s = re.sub(r'\s+', '', string.lower())
        for c in s:
            d[c] = d[c] + 1 if c in d else 1
            num_odd = num_odd + 1 if d[c] % 2 == 1 else num_odd - 1
        if num_odd is 1:
            return True
    return False


string_list = ["Tact Coa",
               "rotator",
               "level",
               "foo",
               "bar",
               "Was it a car or a cat I saw",
               "abca",
               "borrow or rob",
               "",
               None]
fns = [is_palindrome_permutation_naive,
       is_palindrome_permutation]

for fn in fns:
    for string in string_list:
        print(f"{fn.__name__}({string!r}):", fn(string))
    print()


