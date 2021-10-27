"""
    PARENTHESIS COMBINATIONS (CCI 8.9: PARENS,
                              leetcode.com/problems/generate-parentheses)

    Write a function, which accepts an integer n, and returns all valid (e.g., properly opened and closed) combinations
    of n pairs of parenthesis.

    Example:
        Input = 3
        Output = ["((()))", "(()())", "(())()", "()(())", "()()()"]
"""
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Explicitly verify question:
#       + What return type (list of strings)?
#       + What type of parenthesis?
#       + Input validation?


# APPROACH: Naive/Brute Force Recursive
#
# This naive recursive solution adds one pair of parenthesis (for each n), in every possible spot of the previous (n-1)
# calls result.  The only real optimization in this approach is that a set of parenthesis is NOT added to the end of
# each result; technically, this would reduce to the base case, and will always produce duplicates.
#
# NOTE: This IS LESS EFFECTIVE because it waste time creating DUPLICATE combinations (even without adding parens to the
#       end); see next approach.
#
# Time Complexity: O(2 ** (n-1) * (n-1)!), which reduces to O(n!).
# Space Complexity: O(2 ** (n-1) * (n-1)!), which reduces to O(n!).
#
# NOTE: The recurrence relation for this is:
#           f(1) = 1,
#           f(n) = 2 * n-1 * f(n-1).
def parenthesis_combinations_naive(n):
    if isinstance(n, int) and n >= 0:
        if n == 0:
            return [""]
        if n == 1:
            return ["()"]
        result = []
        for i in parenthesis_combinations_naive(n - 1):
            for j in range(len(i)):
                t = i[:j] + "()" + i[j:]
                if t not in result:
                    result.append(t)
        return result


# NOTE/OBSERVATION: All of the remaining approaches count the number of remaining left/right parenthesis (or the
#                   remaining difference/open parenthesis); this is the KEY concept.  COUNT LEFT AND RIGHT PARENS!


# APPROACH: Recursive (Backtracking)
#
# Build a string while maintaining the number of left and right parenthesis that have been used (or appended to the
# accumulator).  Once all (the right and left) parenthesis have been 'used', append the accumulated string to the
# results.
#
# The rules for left/right parenthesis are:
#   Left Paren: As long as we haven't used up all the left paren, we can insert a left paren.
#   Right Paren: We insert a right paren IFF it won't create a syntax error (aka more right than left parens).
#
# NOTE: Because a left and right paren is inserted at each index in the string, and indexes are never repeated, each
#       string is guaranteed to be unique.
#
# Time Complexity: O(catalan(n)), or the nth Catalan Number (basically between O(2**n) and O(n!)).
# Space Complexity: O(catalan(n)), or the nth Catalan Number (basically between O(2**n) and O(n!)).
#
# SEE: https://en.wikipedia.org/wiki/Catalan_number)
def parenthesis_combinations(n):

    def _rec(accumulator, left, right, result):
        if right == 0:                              # NOTE: If right is 0, left will also be 0 (so don't need to check).
            result.append("".join(accumulator))
        if left > 0:
            accumulator.append("(")
            _rec(accumulator, left - 1, right, result)
            accumulator.pop()
        if right > left:
            accumulator.append(")")
            _rec(accumulator, left, right - 1, result)
            accumulator.pop()

    if isinstance(n, int) and n >= 0:
        accumulator = []
        result = []
        _rec(accumulator, n, n, result)
        return result


# APPROACH: (Fastest Recursive) Recursive
#
# This solution uses the same concept as above (counting the number of left and right parenthesis that are remaining),
# however, it concatenates strings (as opposed to building lists then converting to strings).  Therefore, this may be
# easier to follow (or to remember/explain during an interview).
#
# Time Complexity: O(catalan(n)), or the nth Catalan Number (basically between O(2**n) and O(n!)).
# Space Complexity: O(catalan(n)), or the nth Catalan Number (basically between O(2**n) and O(n!)).
def parenthesis_combinations_alt(n):

    def _rec(accumulator, left, right, result=[]):
        if right == 0:                              # NOTE: If right is 0, left will also be 0 (so don't need to check).
            result.append(accumulator)
        if left > 0:
            _rec(accumulator + '(', left - 1, right)
        if right > left:
            _rec(accumulator + ')', left, right - 1)
        return result

    if isinstance(n, int) and n >= 0:
        return _rec('', n, n)


# APPROACH: (Minimized) Recursive
#
# This approach uses a single variable, open, to track the number of unmatched parenthesis (as opposed to two variables,
# left and right).
#
# Time Complexity: O(catalan(n)), or the nth Catalan Number (basically between O(2**n) and O(n!)).
# Space Complexity: O(catalan(n)), or the nth Catalan Number (basically between O(2**n) and O(n!)).
def parenthesis_combinations_min(n, open=0):
    if n > 0 <= open:
        return ['(' + p for p in parenthesis_combinations_min(n-1, open+1)] + \
               [')' + p for p in parenthesis_combinations_min(n, open-1)]
    return [')' * open] * (not n)


# APPROACH: Recursive "Closure Number"
#
# NOTE: This solution comes from leetcode.
# SEE: leetcode.com/problems/generate-parentheses/solution
#
# "To enumerate something, generally we would like to express it as a sum of disjoint subsets that are easier to count."
#
# "Consider the closure number of a valid parentheses sequence S: the least index >= 0 so that S[0], S[1], ...,
#  S[2*index+1] is valid. Clearly, every parentheses sequence has a unique closure number. We can try to enumerate them
#  individually."
#
# "For each closure number c, we know the starting and ending brackets must be at index 0 and 2*c + 1. Then, the 2*c
#  elements between must be a valid sequence, plus the rest of the elements must be a valid sequence."
#
# Time Complexity: O(n**4/log(n)).
# Space Complexity: O(n**4/log(n)).
def parenthesis_combinations_closure(n):
    if isinstance(n, int) and n >= 0:
        if n == 0: return ['']
        result = []
        for c in range(n):
            for left in parenthesis_combinations_closure(c):
                for right in parenthesis_combinations_closure(n-1-c):
                    result.append(f'({left}){right}')
        return result


# APPROACH: Iterative (Via Stack)
#
# This is an iterative version of the recursive approach (above); it uses a list as a stack in place of the recursion
# stack (as in the recursive approach).
#
# Time Complexity: O(catalan(n)), or the nth Catalan Number (basically between O(2**n) and O(n!)).
# Space Complexity: O(catalan(n)), or the nth Catalan Number (basically between O(2**n) and O(n!)).
def parenthesis_combinations_iter(n):
    if isinstance(n, int) and n >= 0:
        result = []
        stack = [('', n, n)]
        while stack:
            accumulator, left, right = stack.pop()
            if right == 0:                      # NOTE: If right is 0, left will also be 0 (so don't need to check).
                result.append(accumulator)
            if left > 0:
                stack.append((accumulator + '(', left-1, right))
            if right > left:
                stack.append((accumulator + ')', left, right-1))
        return result


# APPROACH: Iterative (Via Dynamic Programming)
#
# This approach is included for completeness sake; however, it may be difficult to explain or to conceptualize in an
# interview.
#
# Time Complexity: O(n**4).
# Space Complexity: O(catalan(n)), or the nth Catalan Number (basically between O(2**n) and O(n!)).
def parenthesis_combinations_dp(n):
    if isinstance(n, int) and n >= 0:
        dp = [[] for _ in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += [f'({x})' + y for x in dp[j] for y in dp[i-j-1]]   # here, x + y = n - 1, hence dp[i-j-1]
        return dp[n]


args = [-2, 0, 1, 2, 3, 4, 5, 6]
fns = [parenthesis_combinations_naive,
       parenthesis_combinations,
       parenthesis_combinations_alt,
       parenthesis_combinations_closure,
       parenthesis_combinations_iter,
       parenthesis_combinations_dp]

for n in args:
    print(f"n: {n}")
    for fn in fns:
        print(f"{fn.__name__}(n):", fn(n))
    print()


n = 10
for fn in fns:
    t = time.time()
    print(f"{fn.__name__}({n}) took", end=' ')
    result = fn(n)
    print(f"{time.time() - t} seocnds.")
print()


