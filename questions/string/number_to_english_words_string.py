"""
    NUMBER TO ENGLISH WORDS STRING (leetcode.com/problems/integer-to-english-words/)

    Write a function, which accepts a non-negative natural number num, and returns the numbers representation using
    English words as a string.

    Example:
        Input = 1234567
        Output = "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

"""


# APPROACH: Via Recursion
#
# This approach uses a recursive helper function to break the number into smaller number sections (which are dictated by
# the English language parsing rules, for example; hundreds, thousands, millions), in order build a result list (which
# is converted to a string before being returned).
#
# Time Complexity: O(n), is the number of digits in num.
# Space Complexity: O(n), is the number of digits in num.
def number_to_english_words_string(num):
    ones_and_teens = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
                      'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    d = {10**3: 'Thousand', 10**6: 'Million', 10**9: 'Billion', 10**12: 'Trillion', 10**15: 'Quadrillion',
         10**18: 'Quintillion', 10**21: 'Nonillion', 10**24: 'Decillion'}

    def _rec(n):
        if n == 0:
            return []
        if n < 20:
            return [ones_and_teens[n]]
        if n < 100:                                 # If n is less 100 (and since n is more than 20) just:
            return [tens[n//10]] + _rec(n % 10)         # Find the tens value then (recurse) on the ones value.
        if n < 1000:
            return [ones_and_teens[n//100]] + ['Hundred'] + _rec(n % 100)
        for k, v in d.items():
            if n < 1000 * k:
                return _rec(n//k) + [v] + _rec(n % k)
        return []

    if num == 0:
        return 'Zero'
    if num > 0:
        return " ".join(_rec(num))


args = [0, 1, 2, 5, 9, 10, 11, 13, 18, 19, 20, 21, 69, 100, 101, 110, 111, 123, 1000, 6666, 1000000, 12345, 1234567,
        1234567891]
fns = [number_to_english_words_string]

for num in args:
    print(f"num: {num:,d}")
    for fn in fns:
        print(f"{fn.__name__}(num): {fn(num)}")
    print()


