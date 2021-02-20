"""
    PARENTHESIS CHECKER

    Given a string s representing a mathematical equation (using only digits, +, - , *, /, (, and )), write a function
    that returns True if all brackets and parenthesis are correctly matched False otherwise.  If no brackets or
    parenthesis are included in the equation, return True.

    NOTE: We are ONLY checking that the parenthesis are correctly matched, NOT that the operators/digits are used
    correctly (i.e., "(((+ + 2) / (2 3) * 5) )" would pass our test).

    Example:
        Input = "(((1 + 2) / (2 /3) * 5) )"
        Output = True

        Input = "(1 + (1 / 1) / 3) + 6)"
        Output = False
"""


def parenthesis_checker(s):
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


args = ["(((1 + 2) / (2 /3) * 5) )",
        "(1 + (1 / 1) / 3) + 6)",
        "(((+ + 2) / (2 3) * 5) )",
        ")(",
        "( ) ) (",
        "()()",
        "6 + 9"]

for s in args:
    print(f"parenthesis_checker({s!r}): {parenthesis_checker(s)}")


