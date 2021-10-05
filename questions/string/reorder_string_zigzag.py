"""
    REORDER STRING: ZIGZAG (leetcode.com/problems/zigzag-conversion)

    Write a function, which accepts a string s and a number of rows n, then reorganizes and returns the characters of
    the string according to a (line by line/flattened) zigzag of n rows (please see the examples below) .

    Given the strings "MPETTERSSON" and "Matt", the zigzagged patterns would be:

        M   T   S       M
        P T E S O       a t
        E   R   N       t

    Where the line by line, or flattened strings would be: "MTSPTESOERN" and "Matt".

    Example:
        Input = "MPETTERSSON"
        Output = "MTSPTESOERN"

"""


# APPROACH: Sort (Append) By Row
#
# This approach iterates through the string from left to right, determining which row in the Zig-Zag pattern that the
# current character belongs to, then appending it to the corresponding list in a list of lists.  Once done the lists of
# lists is flattened and returned as a string.
#
# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(n), where n is the length of the string.
def reorder_string_zigzag(s, n):
    if isinstance(s, str) and isinstance(n, int):
        if n == 0:
            return ""
        if n == 1 or n >= len(s):
            return s
        ll = [[] for _ in range(n)]
        row = 0
        flag = False                        # True == Increasing, False == Decreasing
        for i, c in enumerate(s):
            ll[row].append(c)
            if row == 0 or row == n - 1:
                flag = not flag
            row = (row + 1) if flag else (row - 1)
        return ''.join([c for sl in ll for c in sl])


# APPROACH: Compute By Rows
#
# This approach iterates over the rows of the zigzag, to visit the characters in the string.  That is, visit all
# characters in row 0 first, then row 1, then row 2, and so on...
#
# For all whole numbers k:
#   - Characters in row 00 are located at indexes: k * (2 * n - 2)
#   - Characters in row n-1 are located at indexes: k * (2 * n - 2) + n - 1.
#   - Characters in inner row i are located at indexes: k * (2 * n - 2) + i and
#                                                       (k + 1) * (2 * n − 2) - 1.
#
# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(n), where n is the length of the string.
def reorder_string_zigzag_alt(s, n):
    if isinstance(s, str) and isinstance(n, int):
        if n == 0:
            return ""
        if n == 1 or n >= len(s):
            return s
        res = ""
        for r in range(n):
            increment = 2 * (n - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                if 0 < r < n - 1 and i + increment - 2 * r < len(s):
                    res += s[i + increment - 2 * r]
        return res


args = [("MPETTERSSON", 3),
        ("mpettersson", 1),
        ("PAYPALISHIRING",3),
        ("ab", 4),
        ("tacocat", 0),
        ("dqmvxouqesajlmksdawfenyaqtnnfhmqbdcniynwhuywucbjzqxhofdzvposbegkvqqrdehxzgikgtibimupumaetjknrjjuygxvncvjlahdbibatmlobctclgbmihiphshfpymgtmpeneldeygmzlpkwzouvwvqkunihmzzzrqodtepgtnljribmqneumbzusgppodmqdvxjhqwqcztcuoqlqenvuuvgxljcnwqfnvilgqrkibuehactsxphxkiwnubszjflvvuhyfwmkgkmlhmvhygncrtcttioxndbszxsyettklotadmudcybhamlcjhjpsmfvvchduxjngoajclmkxiugdtryzinivuuwlkejcgrscldgmwujfygqrximksecmfzathdytauogffxcmfjsczaxnfzvqmylujfevjwuwwaqwtcllrilyncmkjdztleictdebpkzcdilgdmzmvcllnmuwpqxqjmyoageisiaeknbwzxxezfbfejdfausfproowsyyberhiznfmrtzqtgjkyhutieyqgrzlcfvfvxawbcdaawbeqmzjrnbidnzuxfwnfiqspjtrszetubnjbznnjfjxfwtzhzejahravwmkakqsmuynklmeffangwicghckrcjwtusfpdyxxqqmfcxeurnsrmqyameuvouqspahkvouhsjqvimznbkvmtqqzpqzyqivsmznnyoauezmrgvproomvqiuzjolejptuwbdzwalfcmweqqmvdhejguwlmvkaydjrjkijtrkdezbipxoccicygmmibflxdeoxvudzeobyyrutbcydusjhmlwnfncahxgswxiupgxgvktwkdxumqp", 10),
        (None, None)]
fns = [reorder_string_zigzag,
       reorder_string_zigzag_alt]

for s, n in args:
    print(f"s:{s}\nn:{n}")
    for fn in fns:
        print(f"{fn.__name__}(s, n): {fn(s, n)}")
    print()


