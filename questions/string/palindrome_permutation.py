"""
    PALINDROME PERMUTATION (CCI 1.4)

    Given a string, write a function to check if it is a permutation of a palindrome.  A palindrome is a word or
    phrase that is the same forwards and backwards.  A permutation is a rearrangement of letters.  The paindrome does
    not need to be limited to just a dictionary words.

    Example:
        Input = "Tact Coa"
        Output = True (permutations: "taco cat", "atco cta", etc.)
"""
import re


# This has a runtime of O(n) and a space complexity of O(n).
def is_palindrome_permutation(string):
    if string and len(string) > 0:
        d = dict()
        num_odd = 0
        s = re.sub(r'\s+', '', string.lower())
        for c in s:
            d[c] = d[c] + 1 if c in d else 1
            num_odd = num_odd + 1 if d[c] % 2 == 1 else num_odd - 1
        if num_odd > 1:
            return False
    return True


string_list = ["Tact Coa", "Was it a car or a cat I saw", "abca", "borrow or rob", "", None]

for s in string_list:
    print(f"is_palindrome_permutation(\"{s}\"):", is_palindrome_permutation(s))


