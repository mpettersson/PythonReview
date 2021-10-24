"""
    FIND PALINDROME SUBSTRING PAIRS

    Write a function, which accepts a string s, then finds the (beginning) index pairs of substrings in s that are
    anagrams of each other.

    Two strings are anagrams of each other if the characters of one string can be rearranged to form the other string.

    Example:
        Input = "aaaa"
        Output = [('a', 1, 0), ('a', 2, 0), ('a', 2, 1), ('a', 3, 0), ('a', 3, 1), ('a', 3, 2), ('aa', 1, 0),
                  ('aa', 2, 0), ('aa', 2, 1), ('aaa', 1, 0)]

        NOTE: The substrings are included in the output to improve readability; always ask the interviewer for their
              desired output formatting.
"""
from collections import Counter
from collections import defaultdict


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What are the possible characters?
#   - Should lower case match with upper case?
#   - What are the possible string lengths (empty string)?
#   - What about duplicate palindromes in the list?


# APPROACH: Via Dictionary Of Sorted Characters
#
# This approach constructs a dictionary of sorted characters (key) and the indices where they begin (value), for each
# substring in the string.  After each substring is sorted, if it is in the dictionary, each previously saved index is
# then added to the results (with the current index and the actual substring).  Once all substrings are considered, the
# accumulated results are returned.
#
# Time Complexity: O(n**3 * log(n)), where n is the length of the string.
# Space Complexity: O(n**2), where n is the length of the string.
def find_anagram_substring_pairs_via_sort(s):
    if isinstance(s, str):
        n = len(s)
        result = []
        d = defaultdict(list)                       # d[sorted_string]: number_of_occurrences
        for i in range(n):                          # For all substrings of length 1, then all substrings of length 2,
            for j in range(n - i):                  # etc., until all substrings are enumerated:
                k = ''.join(sorted(s[j:j + i + 1]))         # NLogN - The (anagram) key = sorted substring characters.
                for match in d[k]:
                    result.append((s[j:j + i + 1], j, match))
                d[k].append(j)                      # Maintain the anagrams count.
        return result


# APPROACH: Via Dictionary Of A (Frozenset) Dictionary
#
# This approach only differs from the approach above in the key construction for the dictionary; this approach uses a
# (frozenset) dictionary of characters to their counts (as opposed to a sorted substring) so as to not sort substrings.
# Frozenset is used because it is immutable, and thus, hashable.
#
# Time Complexity: O(n**3), where n is the length of the string.
# Space Complexity: O(n**2), where n is the length of the string.
def find_anagram_substring_pairs_via_dict(s):
    if isinstance(s, str):
        n = len(s)
        result = []
        d = defaultdict(list)                       # d[anagram_frozenset_dict]: number_of_occurrences
        for i in range(n):                          # For each substring start:
            for j in range(i, n):                       # For each substring end:
                k = frozenset(Counter(s[i:j+1]).items())    # O(N) - Build a (frozenset) dict of the substring chars.
                for match in d[k]:
                    result.append((s[i:j+1], j, match))
                d[k].append(j)                      # Maintain the anagrams count.
        return result


string_list = ["mom",                   # 2
               "ifailuhkqq",            # 3
               "abba",                  # 4
               "abcd",                  # 0
               "aaaa",                  # 10
               "cdcd",                  # 5
               "abracadabra",           # 40
               "tacocat",               # 12
               "abcdedcba",             # 20
               "babad",                 # 5
               "rotator",               # 12
               "level",                 # 6
               # "dqmvxouqesajlmksdawfenyaqtnnfhmqbdcniynwhuywucbjzqxhofdzvposbegkvqqrdehxzgikgtibimupumaetjknrjjuygxvncvjlahdbibatmlobctclgbmihiphshfpymgtmpeneldeygmzlpkwzouvwvqkunihmzzzrqodtepgtnljribmqneumbzusgppodmqdvxjhqwqcztcuoqlqenvuuvgxljcnwqfnvilgqrkibuehactsxphxkiwnubszjflvvuhyfwmkgkmlhmvhygncrtcttioxndbszxsyettklotadmudcybhamlcjhjpsmfvvchduxjngoajclmkxiugdtryzinivuuwlkejcgrscldgmwujfygqrximksecmfzathdytauogffxcmfjsczaxnfzvqmylujfevjwuwwaqwtcllrilyncmkjdztleictdebpkzcdilgdmzmvcllnmuwpqxqjmyoageisiaeknbwzxxezfbfejdfausfproowsyyberhiznfmrtzqtgjkyhutieyqgrzlcfvfvxawbcdaawbeqmzjrnbidnzuxfwnfiqspjtrszetubnjbznnjfjxfwtzhzejahravwmkakqsmuynklmeffangwicghckrcjwtusfpdyxxqqmfcxeurnsrmqyameuvouqspahkvouhsjqvimznbkvmtqqzpqzyqivsmznnyoauezmrgvproomvqiuzjolejptuwbdzwalfcmweqqmvdhejguwlmvkaydjrjkijtrkdezbipxoccicygmmibflxdeoxvudzeobyyrutbcydusjhmlwnfncahxgswxiupgxgvktwkdxumqp",     # 31431
               "",                      # 0
               None]
fns = [find_anagram_substring_pairs_via_sort,
       find_anagram_substring_pairs_via_dict]

for s in string_list:
    print(f"s: {s!r}")
    for fn in fns:
        print(f"{fn.__name__}(s): {fn(s)!r}")
    print()


