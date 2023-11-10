"""
    FIND LONGEST COMMON PREFIX (leetcode.com/problems/longest-common-prefix)

    Write a function, which when given a list of strings l, returns the longest common prefix of the strings.

    Example:
        Input = ['flower', 'flow', 'flight']
        Output = 'fl'
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What type of characters will there be?
#   - Should lower case match with upper case?
#   - What are the estimated lengths of the strings?


# APPROACH: Iterative
#
# TODO
#
# Time Complexity: O(n * r), where n is the length of the list and r is the length of the result string.
# Space Complexity: O(1).
def find_longest_common_prefix(l):
    if isinstance(l, list) and all([isinstance(x, str) for x in l]):
        n = len(l)
        if n == 0:
            return
        if n == 1:
            return l[0]
        end = -1
        for i in range(len(min(l, key=len))):       # O(n * 1) bc len is O(1).
            c = l[0][i]
            for j in range(1, n):
                if l[j][i] != c:
                    return l[0][:i]
            end = i
        return l[0][:end+1]


# APPROACH: Iterative
#
# TODO
#
# Time Complexity: O(n * r), where n is the length of the list and r is the length of the result string.
# Space Complexity: O(1).
def find_longest_common_prefix_alt(l):
    if isinstance(l, list) and all([isinstance(x, str) for x in l]):
        result = -1
        n = len(l)
        i = 0
        while True:
            try:
                c = l[0][i]
                for j in range(1, n):
                    if l[j][i] != c:
                        return l[0][:result+1]
                result = i
                i += 1
            except IndexError:
                return l[0][:result+1]


args = [["flower", "flow", "flight"],
        ['ABAB', 'BABA'],
        ['aabcccccaaa', 'aaaaaaaa', 'aaaaaaaa', 'caabccccccaaab'],
        ['aabcccccaaa', 'aaaaaaaa', 'aaaaaaaa', 'aabccccccaaab'],
        ['aaaaa', 'aaaaaaaa', 'aaaaaazaaaa', 'aaaaab'],
        ['a', 'abc', ''],
        ['', 'a', 'abc'],
        ['abc', None],
        None]
fns = [find_longest_common_prefix,
       find_longest_common_prefix_alt]

for l in args:
    print(f"l: {l!r}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l)!r}")
    print()


