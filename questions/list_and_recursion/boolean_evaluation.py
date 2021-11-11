"""
    BOOLEAN EVALUATION (CCI 8.14)

    Given a boolean expression consisting of the symbols 0 (False), 1 (True), & (AND), | (OR), and ^ (XOR), and a
    desired boolean result value result, implement a function to count the number of ways of parenthesizing the
    expression such that it evaluates to result.  The expression should be fully parenthesized (e.g., (0)^(1)) but not
    extraneously (e.g., (((0))^(1))).

    Example:
        Input = "1^0|0|1", False
        Output = 2

        Input = "0&0&0&1^1|0", True
        Output = 10
"""


# Recursive Approach:
def count_eval(s, result):
    if len(s) is 0:
        return 0
    if len(s) is 1:
        return 1 if (False if s is "0" else True) is result else 0
    ways = 0
    for i in range(1, len(s), 2):
        c = s[i]
        left = s[:i]
        right = s[i + 1:]
        left_true = count_eval(left, True)
        left_false = count_eval(left, False)
        right_true = count_eval(right, True)
        right_false = count_eval(right, False)
        total = (left_true + left_false) * (right_true + right_false)
        total_true = 0
        if c is '^':                                                        # Required: One True and one False.
            total_true = left_true * right_false + left_false * right_true
        elif c is '&':                                                      # Required: Both True.
            total_true = left_true * right_true
        elif c is '|':                                                      # Required: Anything but both False.
            total_true = left_true * right_true + left_false * right_true + left_true * right_false
        sub_ways = total_true if result else total - total_true
        ways += sub_ways
    return ways


# Top Down Dynamic Programming (Memoization) Approach:  Same as above, however, use a dictionary to cache the number of
# ways (value) for a given string and result (key).
def count_eval_memo(s, result, memo=None):
    if memo is None:
        memo = {}
    if len(s) is 0:
        return 0
    if len(s) is 1:
        return 1 if (False if s is "0" else True) is result else 0
    if s + str(result) in memo:
        return memo[s+str(result)]
    ways = 0
    for i in range(1, len(s), 2):
        c = s[i]
        left = s[:i]
        right = s[i + 1:]
        left_true = count_eval_memo(left, True, memo)
        left_false = count_eval_memo(left, False, memo)
        right_true = count_eval_memo(right, True, memo)
        right_false = count_eval_memo(right, False, memo)
        total = (left_true + left_false) * (right_true + right_false)
        total_true = 0
        if c is '^':                                                        # Required: One True and one False.
            total_true = left_true * right_false + left_false * right_true
        elif c is '&':                                                      # Required: Both True.
            total_true = left_true * right_true
        elif c is '|':                                                      # Required: Anything but both False.
            total_true = left_true * right_true + left_false * right_true + left_true * right_false
        sub_ways = total_true if result else total - total_true
        ways += sub_ways
    memo[s + str(result)] = ways
    return ways


# Catalan Number Approach:  If you are a genius, you already knew this, but apparently, there's a closed form expression
# that perfectly solves this sequence; the Catalan numbers.
# The expression for the nth Catalan number is: C(n) = ((2n)!)/(n + 1)!n!
# SEE: https://en.wikipedia.org/wiki/Catalan_number for more information on Catalan numbers.


args = [("1^0|0|1", False),         # 2
        ("0&0&0&1^1|0", True),      # 10
        ("0^0&0^1|1", True),        # 10
        ("0^1^0&0^1^0", False),     # 14
        ("0^1^0&0^1^0", True)]      # 28

for s, r in args:
    print(f"count_eval({s}, {r}): {count_eval(s, r)}")
print()

for s, r in args:
    print(f"count_eval_memo({s}, {r}): {count_eval_memo(s, r)}")
print()


