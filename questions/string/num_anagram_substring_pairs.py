"""
    NUM PALINDROME SUBSTRING PAIRS (hackerrank.com/challenges/sherlock-and-anagrams/problem)

    Write a function, which accepts a string s, then finds the number of pairs of substrings in s that are anagrams of
    each other.

    Two strings are anagrams of each other if the characters of one string can be rearranged to form the other string.

    Example:
        Input = "aaaa"
        Output = 10
"""
from collections import Counter


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What are the possible characters?
#   - Should lower case match with upper case?
#   - What are the possible string lengths (empty string)?
#   - What about duplicate palindromes in the list?


# APPROACH: Via Dictionary Of Sorted Characters
#
# This approach first constructs a dictionary of all possible sorted substrings (key) and their number of occurrences
# (value); or a dictionary of possible sorted anagrams (and their counts).  Then, for each key, the number of pairs is
# is calculated (from the occurrences tallied in the first step).  The generic formula (for k number of elements) from
# a set of size n is:
#       n! / (k! * (n - r)!)
# However, for two elements, the formula is reduced to:
#       (n * (n - 1)) / 2
#
# Time Complexity: O(n**3 * log(n)), where n is the length of the string.
# Space Complexity: O(n**2), where n is the length of the string.
def num_anagram_substring_pairs_via_sort(s):
    if isinstance(s, str):
        n = len(s)
        d = {}                                      # d[sorted_string]: number_of_occurrences
        for i in range(n):                          # For all substrings of length 1, then all substrings of length 2,
            for j in range(n - i):                  # etc., until all substrings are enumerated:
                k = ''.join(sorted(s[j:j + i + 1]))         # The (anagram) key is the sorted substring characters.
                d[k] = d.get(k, 0) + 1                      # Maintain the anagrams count.
        result = 0
        for k in d:                                 # For each anagram in the dict:
            result += d[k] * (d[k] - 1) // 2            # Compute, then add, the number of pairs.
        return result


# APPROACH: Via Dictionary Of A (Frozenset) Dictionary
#
# This approach only differs from the approach above in the key construction for the dictionary; this approach uses a
# (frozenset) dictionary of characters to their counts (as opposed to a sorted substring) so as to not sort substrings.
# Frozenset is used because it is immutable, and thus, hashable.
#
# Time Complexity: O(n**3), where n is the length of the string.
# Space Complexity: O(n**2), where n is the length of the string.
def num_anagram_substring_pairs_via_dict(s):
    if isinstance(s, str):
        n = len(s)
        d = {}                                      # d[anagram_frozenset_dict]: number_of_occurrences
        for i in range(n):                          # For each substring start:
            for j in range(i, n):                       # For each substring end:
                k = frozenset(Counter(s[i:j+1]).items())    # O(N) - Build a (frozenset) dict of the substring chars.
                d[k] = d.get(k, 0) + 1                      # Use the (frozenset) dict to count anagrams.
        result = 0
        for k in d:                                 # For each anagram in the dict:
            result += d[k] * (d[k] - 1) // 2            # Compute, then add, the number of pairs.
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
fns = [num_anagram_substring_pairs_via_sort,
       num_anagram_substring_pairs_via_dict]

for s in string_list:
    print(f"s: {s!r}")
    for fn in fns:
        print(f"{fn.__name__}(s): {fn(s)!r}")
    print()


