"""
    STRING COMPRESSION

    Implement a method to perform basic string compression using the counts of repeated chars.
    For example, the string aabcccccaaa would become a2b1c5a3.  If the "compressed" string would not become
    smaller than the original string, your method should return the original string.
    You can assume the string has only uppercase and lowercase letters (a-z).
"""


def string_compression(str):
    if len(str) == 0:
        return str
    curr_count = 1
    curr_char = str[0]
    tmp_str = ""

    for i, c in enumerate(str):
        if i + 1 < len(str) and str[i + 1] == curr_char:
            curr_count += 1
        else:
            tmp_str += "{}{}".format(curr_char, curr_count)
            curr_count = 1
            if i + 1 < len(str):
                curr_char = str[i + 1]

    return tmp_str if len(tmp_str) < len(str) else str


print(string_compression(""))
print(string_compression("aa"))
print(string_compression("abcdefggaa"))
print(string_compression("aabcccccaaa"))


# It's more efficient to determine IF a new string would be SHORTER before actually building it:

def str_compress(str):
    final_len = count_compression(str)
    if final_len >= len(str):
        return str

    tmp_str = ""
    curr_count = 0
    for i in range(len(str)):
        curr_count += 1
        if i + 1 >= len(str) or str[i] != str[i + 1]:
            tmp_str += "{}{}".format(str[i], curr_count)
            curr_count = 0
    return tmp_str


def count_compression(str):
    compressed_len = 0
    curr_count = 0

    for i in range(len(str)):
        curr_count += 1

        if i + 1 >= len(str) or str[i] != str[i + 1]:
            compressed_len += 1 + len("{}".format(curr_count))
            curr_count = 0

    return compressed_len


print(str_compress("abcdefggaa"))


