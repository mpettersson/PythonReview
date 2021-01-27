"""
    STRING COMPRESSION (CCI 1.6: STRING COMPRESSION,
                        50CIQ 48: STRING COMPRESSION)


    Write a function, which accepts a string, and performs a basic string compression that shortens every sequence of
    duplicate characters to a single character followed by the number of duplications.  If the 'compressed' string is
    longer than the original, return the original.

    Example:
        Input = "aabcccccaaa"
        Output = "a2b1c5a3"
"""


# String Concatenation Approach:  First check if a compressed string would actually be shorter than the original string,
# if so, build a compressed return string via string concatenation operand, else, return the original string.
# Runtime Complexity: O(n + k^2), where n is the length of s, and k is the num of char seq.
# Space Complexity: O(n), where n is the length of s.
#
# NOTE:  The quadratic time is due to the inefficiency of the string concatenation (string += string) operand.  IF using
# string concat, it's more efficient to determine IF a new string would be SHORTER before actually building it.
def string_compression_concat(s):

    def _get_compressed_len(s):
        compressed_len = 0
        counter = 0
        s_len = len(s)
        for i in range(len(s)):
            counter += 1
            if i + 1 >= s_len or s[i] != s[i + 1]:
                compressed_len += 1 + len("{}".format(counter))
                counter = 0
        return compressed_len

    if isinstance(s, str):
        if 0 < _get_compressed_len(s) < len(s):
            result = ""
            counter = 0
            s_len = len(s)
            for i in range(len(s)):
                counter += 1
                if i + 1 is s_len or s[i] != s[i+1]:
                    result += "{}{}".format(s[i], counter)
                    counter = 0
            return result
        return s


# Optimal/Direct Approach:
# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(n), where n is the length of the string.
#
# NOTE: If string CONCATENATION was used then the time would be QUADRATIC.
def string_compression(s):
    if isinstance(s, str):
        if len(s) > 2:
            res_list = []
            counter = 0
            for i in range(len(s)):
                counter += 1
                if i+1 is len(s) or s[i+1] != s[i]:
                    res_list.append(f"{s[i]}{counter}")
                    counter = 0
            res_str = ''.join(res_list)
            return res_str if len(res_str) < len(s) else s
        return s


string_list = [None, "", "a", "aa", "AAA", "aaaBBB", "aaabccc", "abcdefggaa", "aabcccccaaa", "caabccccccaaab"]
fns = [string_compression_concat,
       string_compression]

for fn in fns:
    for s in string_list:
        print(f"{fn.__name__}({s!r}): {fn(s)!r}")
    print()


