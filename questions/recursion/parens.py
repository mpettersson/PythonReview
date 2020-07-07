"""
    PARENS

    Implement an algorithm to print all valid (e.g., properly opened and closed) combinations of N pairs of parenthesis.

    Example:
        Input: N = 3
        Output: ((())), (()()), (())(), ()(()), ()()()
"""


# Approach 0 (WRONG): When coming up with this algorithm I only tested a size of 3, which seemed to work...
# NOTE: Make sure you try large n!
def pairs_of_parenthesis_wrong(num):
    if num is 1:
        return ["()"]
    pairs = pairs_of_parenthesis_wrong(num - 1)
    ret_list = []
    for p in pairs:
        if "()" + p not in ret_list:
            ret_list.append("()" + p)
        if p + "()" not in ret_list:
            ret_list.append(p + "()")
        if "(" + p + ")" not in ret_list:
            ret_list.append("(" + p + ")")
    return ret_list


# Approach 1: Recursive approach; build the sol for f(n) by adding pairs of paren to f(n-1).
# This can be done by inserting a pair of paren inside every pair, as well as at the beginning.
# Any other places that we could insert paren, such as the END, would reduce to the base case.
# NOTE: This IS NOT EFFECTIVE because it waste time creating DUPLICATE combinations.
def pairs_of_parenthesis_slow(num):
    values = set()
    if num is 0:
        values.add("")
    else:
        prev = pairs_of_parenthesis_slow(num - 1)
        for s in prev:
            i = 0
            while i < len(s):
                if s[i] is "(":
                    values.add(s[0:i + 1] + "()" + s[i + 1:len(s)])
                i += 1
            values.add("()" + s)
    return values


# Approach 2: Build a string from scratch; on each recursive call we have the index for one char in in the string.
# The rules for left/right parenthesis are:
#   Left Paren: As long as we haven't used up all the left paren, we can insert a left paren.
#   Right Paren: We insert a right paren IFF it won't create a syntax error (aka more right than left parens).
# NOTE: Because a left and right paren is inserted at each index in the string, and indexes are never repeated,
# each string is guaranteed to be unique.
def pairs_of_parenthesis(num):
    char_list = [None] * (2 * num)
    values = []
    _pairs_of_parenthesis(values, num, num, char_list, 0)
    return values


def _pairs_of_parenthesis(values, left_rem, right_rem, char_list, count):
    if left_rem < 0 or right_rem < left_rem:
        return
    if left_rem == 0 and right_rem == 0:
        values.append("".join(char_list))
    else:
        if left_rem > 0:
            char_list[count] = "("
            _pairs_of_parenthesis(values, left_rem - 1, right_rem, char_list, count + 1)
        if right_rem > left_rem:
            char_list[count] = ")"
            _pairs_of_parenthesis(values, left_rem, right_rem - 1, char_list, count + 1)


few = 3
print("few:", few)
print("len(pairs_of_parenthesis_wrong(few)):", len(pairs_of_parenthesis_wrong(few)))
print("len(pairs_of_parenthesis_slow(few)):", len(pairs_of_parenthesis_slow(few)))
print("len(pairs_of_parenthesis(few)):", len(pairs_of_parenthesis(few)))
print()

several = 6
print("several:", several)
print("len(pairs_of_parenthesis_wrong(several)):", len(pairs_of_parenthesis_wrong(several)))
print("len(pairs_of_parenthesis_slow(several)):", len(pairs_of_parenthesis_slow(several)))
print("len(pairs_of_parenthesis(several)):", len(pairs_of_parenthesis(several)))
print()

lots = 12
print("lots:", lots)
import time
t = time.time()
print("len(pairs_of_parenthesis_wrong(lots)):", len(pairs_of_parenthesis_wrong(lots)), "took:", time.time() - t)
t = time.time()
print("len(pairs_of_parenthesis_slow(lots)):", len(pairs_of_parenthesis_slow(lots)), "took:", time.time() - t)
t = time.time()
print("len(pairs_of_parenthesis(lots)):", len(pairs_of_parenthesis(lots)), "took:", time.time() - t)
print()


