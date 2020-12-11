"""
    ROMAN NUMERAL FROM DECIMAL

    Write a function, which accepts a positive (integer) number less than 4000, that converts and returns the number to
    a string of roman numerals. Pertinent information on roman numerals:

    Roman Numerals are composed from seven symbols:
        I: 1
        V: 5
        X: 10
        L: 50
        C: 100
        D: 500
        M: 1000

    NOTE: There is no (Roman numeral) symbol for zero; however, the latin word 'nulla' was used for none.

    The rules for Roman Numerals:
        1: When a smaller symbol is after a greater symbol, it's added.
        2: If a symbol comes after itself, it's added.
        3: When a smaller power of ten symbol appears before a greater symbol, that is at most ten times the smaller
           symbol, it is subtracted.  That is, only IV, IX, XL, XC, CD, and CM are valid subtractions.
        4: The symbols I, X, C, and M can be used up to three times in a row.
        5: The symbols V, L, and D cannot be repeated.
        6: A bar placed on top of a symbol increases the symbols' value by 1,000 times (i.e., V bar bar is 5000).

    NOTE: Use the following sentence to help remember the order: My   Dear Cat Loves Xtra Vanilla Ice-cream.
                                                                 1000 500  100 50    10   5       1
    Example:
        Input = 3549
        Output = "MMMDXLIX"  # NOT: "MMMDIL", this is because rule
"""
import re


# Approach:  Once you KNOW THE RULES this is very simple.
# Time Complexity: O(n), where n is the length of the Roman numeral string.
# Space Complexity: O(1).
def roman_numeral_from_decimal(number):
    if number and 0 < number < 4000:
        result = ""
        mapping = [[1000, 'M'],
                   [900, 'CM'],
                   [500, 'D'],
                   [400, 'CD'],
                   [100, 'C'],
                   [90, 'XC'],
                   [50, 'L'],
                   [40, 'XL'],
                   [10, 'X'],
                   [9, 'IX'],
                   [5, 'V'],
                   [4, 'IV'],
                   [1, 'I']]
        i = 0
        while number:
            if number >= mapping[i][0]:
                number -= mapping[i][0]
                result += mapping[i][1]
            else:
                i += 1
        return result


# Strict Roman Numeral Checker
# SEE: https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch06s09.html
def is_valid_roman_numeral(string):
    if string:
        pattern = r"^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"
        if re.match(pattern, string):
            return True
    return False


numbers = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 42, 99, 420, 999, 1000, 2020, 3549, 3999, 4000, None]
for number in numbers:
    print(f"roman_numeral_from_decimal({number}): {roman_numeral_from_decimal(number)!r}")


