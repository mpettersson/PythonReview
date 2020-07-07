"""
    ADD ONE

    Design an algorithm that will add one to a given a list of single digits representing a number.

    Example:
        Input =  [1, 0, 0, 3]
        Output = [1, 0, 0, 4]

    NOTE: Variations of this problem could be:
            - Add/Subtract a given value.
            - Add/Subtract two lists representing values.
"""


# Simple Approach: The time and space complexity is O(n).
def add_one(l):
    carry = 1
    result = [0] * len(l)
    for i in reversed(range(len(l))):
        total = l[i] + carry
        carry = 1 if total is 10 else 0
        result[i] = total % 10
    if carry == 1:
        result = [1] + result
    return result


lists = [[1, 0, 0, 3],
         [0],
         [9],
         [9, 9, 9, 9, 9, 9]]

for l in lists:
    print(f"add_one({l}):", add_one(l))







