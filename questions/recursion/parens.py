"""
    PARENS (CCI 8.9)

    Implement an algorithm to print all valid (e.g., properly opened and closed) combinations of N pairs of parenthesis.

    Example:
        Input: N = 3
        Output: ((())), (()()), (())(), ()(()), ()()()
"""
import time


# Approach 0 (WRONG): When coming up with this algorithm I only tested a size of 3, which seemed to work...
# NOTE: Make sure you try large n!
def parens_wrong(n):
    if n is not None and n > 0:
        if n is 1:
            return ["()"]
        pairs = parens_wrong(n - 1)
        ret_list = []
        for p in pairs:
            if "()" + p not in ret_list:
                ret_list.append("()" + p)
            if p + "()" not in ret_list:
                ret_list.append(p + "()")
            if "(" + p + ")" not in ret_list:
                ret_list.append("(" + p + ")")
        return ret_list


# Naive Recursive Approach 1: Build the solution for f(n) by adding pairs of paren to f(n-1).  This can be accomplished
# by inserting a pair of parens at the beginning and inside every pair of n-1 parens.  Observe that adding parens at the
# END would reduce to the base case.  This IS NOT EFFECTIVE because it waste time creating DUPLICATE combinations.
# Time and space complexity is O(n!) (or, more exactly, it is O(2**(n-1) * (n-1)!), the recurrence relation for size is:
# f(1) = 1, f(n) = 2 * n-1 * f(n-1).)
def parens_naive(n):
    if n is not None and n >= 0:
        if n is 0:
            return [""]
        if n is 1:
            return ["()"]
        values = []
        for i in parens_naive(n - 1):
            for j in range(len(i)):
                t = i[:j] + "()" + i[j:]
                if t not in values:
                    values.append(t)
        return values


# Approach 2: Build a string from scratch; on each recursive call we have the index for one char in in the string.
# The rules for left/right parenthesis are:
#   Left Paren: As long as we haven't used up all the left paren, we can insert a left paren.
#   Right Paren: We insert a right paren IFF it won't create a syntax error (aka more right than left parens).
# NOTE: Because a left and right paren is inserted at each index in the string, and indexes are never repeated,
# each string is guaranteed to be unique.
# Time and space complexity is between O(2**n) and O(n!).
def parens(n):

    def _parens(values, l_parens, r_parens, char_list, i):
        if 0 <= l_parens <= r_parens:
            if l_parens is 0 and r_parens is 0:
                values.append("".join(char_list))
            else:
                if l_parens > 0:
                    char_list[i] = "("
                    _parens(values, l_parens - 1, r_parens, char_list, i + 1)
                if r_parens > l_parens:
                    char_list[i] = ")"
                    _parens(values, l_parens, r_parens - 1, char_list, i + 1)

    if n is not None and n >= 0:
        char_list = [None] * (2 * n)
        values = []
        _parens(values, n, n, char_list, 0)
        return values


args = [-2, 0, 1, 2, 3, 4, 5]

for a in args:
    print(f"parens_wrong({a}):", parens_wrong(a))
print()

for a in args:
    print(f"parens_naive({a}):", parens_naive(a))
print()

for a in args:
    print(f"parens({a}):", parens(a))
print()

a = 10
t = time.time(); values = parens_wrong(a); print(f"parens_wrong({a}) (took {time.time() - t} seconds): {values}")
t = time.time(); values = parens_naive(a); print(f"parens_naive({a}) (took {time.time() - t} seconds): {values}")
t = time.time(); values = parens(a); print(f"parens({a}) (took {time.time() - t} seconds): {values}")


