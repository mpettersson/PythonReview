"""
    STRING COMPRESSION (CCI 1.6)

    Implement a method to perform basic string compression using the counts of repeated chars.
    For example, the string aabcccccaaa would become a2b1c5a3.  If the "compressed" string would not become
    smaller than the original string, your method should return the original string.
    You can assume the string has only uppercase and lowercase letters (a-z).

    Example:
        Input = "aabcccccaaa"
        Output = "a2b1c5a3"
"""


# Direct Approach: Time and Space Complexity of O(p), where p is the length of the string s.
# NOTE: If string CONCATENATION was used then the time would be QUADRATIC.
def string_compression(s):
    if not s or len(s) < 3:
        return s
    cur_count = 1
    i = 0
    res = []
    while i < len(s):
        if i + 1 < len(s) and s[i + 1] == s[i]:
            cur_count += 1
        else:
            res.append(s[i])
            res.append(str(cur_count))
            cur_count = 1
        i += 1
    result = "".join(res)
    return result if len(result) < len(s) else s


# String Concatenation Approach: Runtime is O(p + k^2) where p is len(s) and k is the num of char seq. Space is O(p).
# The quadratic time is due to the inefficiency of the string concatenation (string += string) operand.
# IF using string concat, it's more efficient to determine IF a new string would be SHORTER before actually building it:
def string_compression_alternative(s):
    if not s:
        return s
    final_len = count_compression(s)
    if final_len >= len(s):
        return s
    tmp_str = ""
    curr_count = 0
    for i in range(len(s)):
        curr_count += 1
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            tmp_str += "{}{}".format(s[i], curr_count)
            curr_count = 0
    return tmp_str


def count_compression(s):
    compressed_len = 0
    curr_count = 0
    for i in range(len(s)):
        curr_count += 1
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            compressed_len += 1 + len("{}".format(curr_count))
            curr_count = 0
    return compressed_len


string_list = [None, "", "a", "aa", "abcdefggaa", "aabcccccaaa", "caabccccccaaab"]

for s in string_list:
    print(f"string_compression({s!r}): {string_compression(s)!r}")
print()

for s in string_list:
    print(f"str_compress({s!r}): {string_compression_alternative(s)!r}")


