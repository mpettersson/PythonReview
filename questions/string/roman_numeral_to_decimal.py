"""
    ROMAN NUMERAL TO DECIMAL

    Write a function, which accepts a string s, of roman numerals, and returns the decimal/integer value of the string.
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
           symbol, it is subtracted.
           That is, there are only six instances where subtraction is used:
              - IV, IX,
              - XL, XC,
              - CD, and CM are valid subtractions.
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


# APPROACH: Via Dict
#
# Once you KNOW THE RULES this is very simple.  Iterate over all of the numeral/char, excluding the last one (it'll be
# handled in a bit); if the current numeral/char is less than the following char (since we are excluding the last char
# from the loop, we don't need to check length) subtract the value from the results, else, add the value to the results.
# The last value, even if it is a part of a subtraction case, is added (i.e., 'IV", is a subtraction case, but the five
# is added), so add the last numeral's value to the results.  Then, return the results.
#
# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(1).
def roman_numeral_to_decimal(s):
    result = 0
    if isinstance(s, str) and len(s) > 0:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s)-1):           # The last numeral/char is a special case, and is done at end/outside loop.
            if d[s[i]] < d[s[i + 1]]:       # If the current numeral/char is less than the next one (subtraction case):
                result -= d[s[i]]               # Subtract it!
            else:                           # Else:
                result += d[s[i]]               # Add it!
        result += d[s[-1]]                  # Even if the last numeral is used in a sub case, it is still added to res.
    return result


# APPROACH: Via Dict Verbose
#
# Once you KNOW THE RULES this is very simple; use a lookup table (dict) to map the characters to their values.  Then
# iterate over the characters, first, looking for any of the six subtraction cases (i.e., that there are at least two
# remaining chars and the one with the smaller value is first).  If a subtraction case is found, simply add the larger
# (second) value and subtract the smaller (first) value.  If not a subtraction case then simply add the mapped value to
# the results.  Once done, return the computed results.
#
# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(1).
def roman_numeral_to_decimal_verbose(s):
    if isinstance(s, str):
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        result = 0
        while i < len(s):
            if i + 1 < len(s) and d[s[i + 1]] > d[s[i]]:    # If subtraction case (need smaller then larger char):
                result += d[s[i + 1]] - d[s[i]]                 # Add (larger - smaller) to the results.
                i += 2                                          # And increment the counter by two (since two chars).
            else:                                           # Else:
                result += d[s[i]]                               # Add the result of whatever the value of the char is.
                i += 1                                          # And increment the counter by one (just one char).
        return result


# BONUS: Strict Roman Numeral Checker
# SEE: https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch06s09.html
def is_valid_roman_numeral(s):
    if s:
        pattern = r"^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"
        if re.match(pattern, s):
            return True
    return False


args = [None, "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XXX", "LXIX", "MMXX",
        "IC",                       # Invalid Rule 3
        "LXLIX",                    # Invalid Rule 3
        "XCIX",                     # Valid
        "MMMDDDCCCLLLXXXVVVIII",    # Invalid Rule 5
        "MMMCMXCIX",                # Valid
        "MMMIMIMIMIMIMIMIMIMIM"]    # Invalid Rule 3
fns = [roman_numeral_to_decimal,
       roman_numeral_to_decimal_verbose]

for s in args:
    for fn in fns:
        print(f"{fn.__name__}({s!r}): {fn(s)}")
    print()


