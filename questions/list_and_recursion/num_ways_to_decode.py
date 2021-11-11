"""
    NUM WAYS TO DECODE

    Given a string of digits that represents an encoded message (data), write a method to count the number of ways to
    decode the message.  You can assume that the message (data) only contains the characters zero through nine [0-9].

    The encoding function is:
        'a' --> 1
        'b' --> 2
             .
             .
             .
        'y' --> 25
        'z' --> 26

    Example:
        Input = "12"
        Output = 2 ("12" can represent "ab" OR "l")
"""


# Recursive Approach: O(2**n) time, O(1) space.
def num_ways_to_decode_recursive(data):

    def _num_ways_to_decode_recursive(data, k):
        if k == 0:
            return 1
        start = len(data) - k
        if data[start] == '0':
            return 0
        result = _num_ways_to_decode_recursive(data, k - 1)
        if k >= 2 and int(data[start:start+2]) <= 26:
            result += _num_ways_to_decode_recursive(data, k - 2)
        return result

    return _num_ways_to_decode_recursive(data, len(data))


# Top Down Dynamic Programming Approach: O(n) time, O(n) space.
def num_ways_to_decode_tddp(data):
    memo = [None] * (len(data) + 1)

    def _num_ways_to_decode_tddp(data, k, l):
        if k == 0:
            return 1
        start = len(data) - k
        if data[start] == '0':
            return 0
        if l[k]:
            return l[k]
        l[k] = _num_ways_to_decode_tddp(data, k - 1, l)
        if k >= 2 and int(data[start:start+2]) <= 26:
            l[k] += _num_ways_to_decode_tddp(data, k - 2, l)
        return l[k]

    return _num_ways_to_decode_tddp(data, len(data), memo)


inputs = ["3", "", "12345", "111111", "27345", "101", "011"]  # NOTE: "101" is valid, "011" is NOT valid.

for i in inputs:
    print(f"num_ways_to_decode_recursive({i}):", num_ways_to_decode_recursive(i))
print()

for i in inputs:
    print(f"num_ways_to_decode_tddp({i}):", num_ways_to_decode_tddp(i))

