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


def string_compression(s):
    if not s or len(s) <= 1:
        return s
    curr_count = 1
    curr_char = s[0]
    tmp_str = ""
    for i, c in enumerate(s):
        if i + 1 < len(s) and s[i + 1] == curr_char:
            curr_count += 1
        else:
            tmp_str += "{}{}".format(curr_char, curr_count)
            curr_count = 1
            if i + 1 < len(s):
                curr_char = s[i + 1]
    return tmp_str if len(tmp_str) < len(s) else s


# It's more efficient to determine IF a new string would be SHORTER before actually building it:
def efficient_string_compression(s):
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


string_list = [None, "", "a", "abcdefggaa", "aabcccccaaa"]

for s in string_list:
    print(f"string_compression({s}):", string_compression(s))
print()

for s in string_list:
    print(f"str_compress({s}):", efficient_string_compression(s))


