"""
    PARENTHESIS VALIDATOR (leetcode.com/problems/valid-parentheses)

    Write a function that accepts a string s containing only the characters '(', ')', '{', '}', '[' and ']', then
    returns True if the input string is valid, False otherwise.  An input string is valid if:
        - Brackets are closed by the same type brackets.
        - Open brackets are closed in the correct order.

    Example:
        Input = '()[]{}'
        Output = True
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Explicitly verify question:
#       + Only checking parenthesis, NOT checking operators/operands?
#       + What types of parenthesis (just () {} and [])?
#       + Input validation?


# APPROACH: Via Stack
#
# This approach uses a stack to track the last opened parenthesis and a dictionary to match the different types of
# parenthesis.
#
# Time Complexity: O(n), where n is the number of characters in the string.
# Space Complexity: O(1).
def is_valid_parenthesization(s):
    if isinstance(s, str):
        if len(list(s)) % 2 == 1:           # Don't forget to do a quick check, might save a lot of time....
            return False
        stack = []
        d = {"]": "[", "}": "{", ")": "("}
        for c in s:
            if c in d.values():
                stack.append(c)
            elif c in d.keys():
                if stack == [] or d[c] != stack.pop():
                    return False
            else:
                return False
        return stack == []


# APPROACH: Via Stack
#
# This is the same as above, just with two lists as opposed to a dictionary.
#
# Time Complexity: O(n), where n is the number of characters in the string.
# Space Complexity: O(1).
def is_valid_parenthesization_alt(s):
    if isinstance(s, str):
        if len(list(s)) % 2 == 1:           # Don't forget to do a quick check, might save a lot of time....
            return False
        stack = []
        op = ['(', '{', '[']
        cl = [')', '}', ']']
        for c in s:
            if c in op:
                stack.append(cl[op.index(c)])
            elif len(stack) != 0 and c == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0


args = ["()",                           # True
        "()[]{}",                       # True
        "(]",                           # False
        ")(",                           # False
        "())(",                         # False
        "()()",                         # True
        "([)]",                         # False
        "",                             # True
        "{[]}",                         # True
        None]
fns = [is_valid_parenthesization,
       is_valid_parenthesization_alt]

for s in args:
    for fn in fns:
        print(f"{fn.__name__}({s!r}): {fn(s)}")
    print()


