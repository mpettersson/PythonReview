"""
    ROMAN NUMERAL TO DECIMAL

    Write a function, which accepts a string of roman numerals, and returns the decimal/integer value of the string.
    Pertinent information on roman numerals:

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
        Input = 'MMMCMXCIX'
        Output = 3999
"""
import re


# Approach:  Once you KNOW THE RULES this is very simple.
# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(1).
def roman_numeral_to_decimal(string):
    if string:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        result = 0
        while i < len(string):
            if i + 1 < len(string) and d[string[i + 1]] > d[string[i]]:
                result += d[string[i + 1]] - d[string[i]]
                i += 1
            else:
                result += d[string[i]]
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


args = [None, "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XXX", "LXIX", "MMXX",
        "IC",                       # Invalid Rule 3
        "LXLIX",                    # Invalid Rule 3
        "XCIX",                     # Valid
        "MMMDDDCCCLLLXXXVVVIII",    # Invalid Rule 5
        "MMMCMXCIX",                # Valid
        "MMMIMIMIMIMIMIMIMIMIM"]    # Invalid Rule 3

for s in args:
    print(f"is_valid_roman_numeral({s!r}): {is_valid_roman_numeral(s)}")
print()

for s in args:
    print(f"roman_numeral_to_decimal({s!r}): {roman_numeral_to_decimal(s)}")


