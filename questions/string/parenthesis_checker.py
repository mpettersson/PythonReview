"""
    PARENTHESIS CHECKER

    Given a string s representing a mathematical equation (using only digits, +, - , *, /, (, and )), write a function
    that returns True if all parenthesis are correctly matched False otherwise.  If no parenthesis are included in the
    equation, return True.

    NOTE: This question ONLY checks if the parenthesis are correctly matched, NOT that the operators/digits are used
    correctly (i.e., "(((+ + 2) / (2 3) * 5) )" would pass).

    Example:
        Input = "(((1 + 2) / (2 / 3) * 5) )"
        Output = True

        Input = "(1 + (1 / 1) / 3) + 6)"
        Output = False

    Variations:
        - Same question, however, the asterisks is now a wild card representing either an open paren, close paren, or
          mathematical operator.  SEE: https://leetcode.com/problems/valid-parenthesis-string/
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Explicitly verify question:
#       + Only checking parenthesis, NOT checking operators/operands?
#       + No decimals?
#       + What about other types of parenthesis (or {} and [])?
#       + Input validation?


# APPROACH: Via Counter
#
# Iterate over the individual characters in the equation, using a counter to track the state of the parenthesis; if at
# any point the counter goes negative return False, finally, return True if the counter is zero, False otherwise.
#
# Time Complexity: O(n), where n is the number of characters in the string.
# Space Complexity: O(1).
def is_valid_parenthesizations(s):
    if s is not None:
        parens = 0
        for c in s:
            if c == '(':
                parens += 1
            elif c == ')':
                parens -= 1
                if parens < 0:
                    return False
        return True if parens == 0 else False
    return False


# VARIATION:  Same question, however, the asterisks is now a wild card.


# VARIATION APPROACH: Asterisks Wildcard Via Counters
#
# This approach is similar to the above (original question) approach, however, an additional counter (so, one for the
# minimum number of parenthesis and one for the maximum number of parenthesis) is required to verify asterisks usage.
#
# Time Complexity: O(n), where n is the number of characters in the string.
# Space Complexity: O(1).
def is_valid_parenthesizations_with_asterisks_wildcard(s):
    if s is not None:
        parens_min = 0                          # The smallest (lower bound) num of ')' parens needed.
        parens_max = 0                          # The largest (upper bound) num of ')' parens needed
        for c in s:
            if c == '(':                        # Both counters increase.
                parens_min += 1
                parens_max += 1
            elif c == ')':                      # Both counters decrease.
                parens_min -= 1
                parens_max -= 1
            elif c == '*':                      # Widen the possible range:
                parens_min -= 1                     # Decrease the lower bound; use the '*' as a ')'.
                parens_max += 1                     # Increase the upper bound; use the '*' as a '('.
            if parens_max < 0:                  # If upper bound ever drops below 0, then fail.
                return False
            parens_min = max(parens_min, 0)     # If parens_min < 0, reset to 0, or use a '*'; the ↑ & ↓ bounds tighten.
        return True if parens_min == 0 else False   # We know parens_max >= 0. Only check there aren't too many '('.
    return False


# VARIATION APPROACH: Asterisks Wildcard Via Stacks
#
# Iterate over the characters, using two stacks to maintain the indices of left parens and the asterisks, whenever a
# right parenthesis is encountered pop from the left parenthesis stack (if populated), or pop from the asterisks stack
# (if populated), or return False.  Finally, compare the length of the stacks to ensure that the the number of asterisks
# is greater than or equal to the left parens AND that corresponding (closing) asterisks are AFTER the opening parens.
#
# Time Complexity: O(n), where n is the number of characters in the string.
# Space Complexity: O(n), where n is the number of characters in the string.
def is_valid_parenthesizations_via_stacks_with_asterisks_wildcard(s):
    if s is not None:
        l_paren_stack = []
        asterisk_stack = []
        for i, c in enumerate(s):
            if c == '(':
                l_paren_stack.append(i)
            elif c == '*':
                asterisk_stack.append(i)
            elif c != ')':
                continue
            else:   # c == ')'                                          Have a ')':
                if len(l_paren_stack) == 0 and len(asterisk_stack) == 0:    # Case 1: No matching '*' or '('.
                    return False
                if len(l_paren_stack) > 0:                                  # Case 2: Have one or more '('.
                    l_paren_stack.pop()
                else:                                                       # Case 3: No matching '(', one or more '*'.
                    asterisk_stack.pop()
        while l_paren_stack and asterisk_stack:
            if l_paren_stack.pop() > asterisk_stack.pop():      # NOTE: This check is important; asterisks must occur
                return False                                          # AFTER left parens to close the open paren!
        return len(l_paren_stack) == 0
    return False


args = ["(((1 + 2) / (2 /3) * 5) )",
        "(1 + (1 / 1) / 3) + 6)",
        "(((+ + 2) / (2 3) * 5) )",
        ")(",
        "( ) ) (",
        "()()",
        "6 + 9 / *",
        "6 * 9",
        "(*)",
        "*)",
        "(*",
        "9",
        "*",
        None]
fns = [is_valid_parenthesizations,
       is_valid_parenthesizations_with_asterisks_wildcard,                  # Variation
       is_valid_parenthesizations_via_stacks_with_asterisks_wildcard]       # Variation

for s in args:
    for fn in fns:
        print(f"{fn.__name__}({s!r}): {fn(s)}")
    print()


