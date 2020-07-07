"""
    CALCULATOR

    Given an arithmetic equation consisting of positive integers, +, -, *, and / (no parentheses), compute the result.

    Example:
        input = "2*3+5/6*3+15"
        output = 23.5
"""
import operator
import re


# Compute the result of given sequence; works by reading left to right and applying each term to a result.
# When we see a * or /, we instead apply this sequence to a temp variable (processing).
def compute(sequence):
    terms = parse_term_sequence(sequence)
    if terms is None:
        return None
    result = 0
    processing = None
    for i, current in enumerate(terms):
        next_op = terms[i + 1].operator if i + 1 < len(terms) else None
        processing = collapse_term(processing, current)
        # If next term is + or -, then this cluster is done and we should apply "processing" to "result"
        if next_op is None or next_op is operator.add or next_op is operator.sub:
            result = apply_op(result, processing.operator, processing.value)
            processing = None
    return result


# Collapse two terms together using the operator in secondary and the numbers from each.
def collapse_term(primary, secondary):
    if primary is None:
        return secondary
    if secondary is None:
        return primary
    value = apply_op(primary.get_number(), secondary.get_operator(), secondary.get_number())
    primary.set_number(value)
    return primary


def apply_op(left, op, right):
    return (lambda l, r, f: f(l, r))(left, right, op)


def get_op(s):
    if s == "":  # If it's nothing, it means it was first, we'll use add so it can and with 0 (start value).
        return operator.add
    elif s == "+":
        return operator.add
    elif s == "-":
        return operator.sub
    elif s == "/":
        return operator.truediv
    elif s == "*":
        return operator.mul
    else:
        raise ValueError


# Parse arithmetic sequence into a list of Terms; if improperly formatted, returns None.
def parse_term_sequence(sequence):
    if re.search(r'^(-?\d*\.?\d+)((\+|\-|\*|\/)(-?\d*\.?\d+))*$', sequence):
        pattern = r'((?P<operator>[+\-\*\/]?)(?P<numbers>\-?\d*\.?\d+))'
        dict_list = [m.groupdict() for m in re.finditer(pattern, sequence)]
        terms = []
        for d in dict_list:
            terms.append(Term(float(d["numbers"]), get_op(d["operator"])))
        return terms
    else:
        return None


class Term:
    def __init__(self, value, operator=None):
        self.value = value
        self.operator = operator

    def get_number(self):
        return self.value

    def get_operator(self):
        return self.operator

    def set_number(self, value):
        self.value = value


eq_str_list = ["4---1", "2--4", "2*3+5/6*3+15", "-84.8/89.9", "3+8+9-8", "5++4",  "+5*8", "5*8", "+10", "10", "-10"]
for eq in eq_str_list:
    print("compute(", eq, ") = ", compute(eq))






