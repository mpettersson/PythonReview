"""
    BEDBATHANDBEYOND (EPI 17.7: THE BEDBATHANDBEYOND.COM PROBLEM)

    Consider the following scenario:
        Suppose you are designing a search engine. You tasks are to obtain keywords from a page's content as well as
        from the Uniform Resource Locators (URLs). For example, given the URL bedbathandbeyoond.com, the obtained
        keywords are; "bed, bath, beyond, bat, hand" (where "bed" and "bath" from the decomposition of "bed bath beyond"
        and "beyond", "bat", "hand" coming from the decomposition "bed bat hand beyond").

    Write a function, which when given a dictionary set of strings, and a name, checks whether the name is in the
    concatenation of a sequence of dictionary words; return it if such a concatenation exists, else, None.

    NOTE: A dictionary word may appear more than once in the sequence.

    Example:
        Input = {"a", "bat", "bath", "bed", "beyond", "canal", "hand", "man", "plan"}, "amanaplanacanal"
        Output = ["a", "man", "a", "plan", "a", "canal"]
"""
import itertools


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What data structure is the dictionary set (verify it isn't ordered)?
#   - Can the dictionary set be modified?
#   - What is the character set?
#   - Will there be both upper and lower case?
#   - What are the possible string lengths in the dictionary/url (empty string)?
#   - What happens if the dictionary is empty?


# APPROACH: Via Brute Force
#
# This approach uses the itertools combinations function to generate all possible partition points of the string, where
# a generator then yields the partitioned string.  Each of the string partitions are then checked against for membership
# in the dictionary; once (while checking any of the string partitions) all of the string partitions are in the
# dictionary, then that particular list of string partitions is returned.
#
# NOTE: This only returns the first of any such concatenations.
#
# Time Complexity: O(2**n), where n is the length of the string.
# Space Complexity: O(n), where n is the length of the string.
def decompose_into_dictionary_set_via_bf(string, dictionary_set):

    def gen_all_string_partitions_via_itertools_comb(s):    # This is a generator for all partitions of s.

        def _gen_string_partitions_at_points(s, points):    # This does the actual slicing.
            length = len(points)
            if length > 0:
                s_slices = [s[:points[0]]]
                s_slices.extend(s[points[i]:points[i + 1]] for i in range(length - 1))
                s_slices.append(s[points[length - 1]:])
                return s_slices
            return [s]

        for r in range(len(s)):
            for cut_points in itertools.combinations(list(range(1, len(s))), r):
                yield _gen_string_partitions_at_points(s, cut_points)

    if string is not None and dictionary_set is not None:
        for string_partitions_i in gen_all_string_partitions_via_itertools_comb(string):
            if all(map(lambda x: x in dictionary_set, string_partitions_i)):    # Are all of str partitions in the dict.
                return list(string_partitions_i)                                # Return first match.


# APPROACH: Via Naive Recursion
#
# This is simply a recursive brute force approach approach; starting at the beginning, slices are checked against the
# dictionary; if the current slice isn't in the dictionary then the slice is lengthened by one then tried again.  When
# a slice is in the dictionary, the slice is added to an accumulator (list of string slices) then the recursion
# continues at the end of the slice.  If the starting index ever reaches the end of the string (is equal to the size of
# the string), then the accumulated results are returned.
#
# Time Complexity: O(2**n), where n is the length of the string.
# Space Complexity: O(n), where n is the length of the string.
def decompose_into_dictionary_set_rec(string, dictionary_set):

    def _rec(i_start, accumulator):
        if i_start == len(string):                  # If the starting index == length of the string, job done;
            return accumulator                          # Return the accumulated string partitions.
        if i_start < len(string):                   # If the starting index < length of the string;
            i_end = i_start + 1                         # initialize an ending index as the next index (after start),
            while i_end <= len(string):                     # while the ending index is in the string boundaries;
                if string[i_start: i_end] in dictionary_set:    # If the string slice from start to end in in the dict:
                    res = _rec(i_end, accumulator + [string[i_start: i_end]])   # Recurse from then end.
                    if res is not None:                             # If the recursion returned a value:
                        return res                                      # Return the FIRST string partition list!
                i_end += 1                                      # Else, increment the end and try again...

    if string is not None and dictionary_set is not None:
        return _rec(0, [])


# APPROACH: Tabulation/Bottom Up Dynamic Programming
#
# This approach uses a cache, or memoization table, to store previously matched substrings.  It iterates over the string
# starting with a substring of length one, to the length of the string.  If any of the string slices (that always start
# at the beginning of the string) are in the dictionary, then the cache is updated (the length of the matched string is
# inserted at the ENDING index of that string).  If, however, the slice (starting at the beginning of the string) is NOT
# in the dictionary, then one more iteration occurs, starting from the beginning to the current index.  This second
# iteration looks for a match from a previous match to the current position.  The first such match is then used and
# is marked in the cache table (i.e., the length of the smaller 'connecting' word is placed at the corresponding end
# index in the cache). Once all slices (including the check for the full word) has been checked, IF the last value in
# the cache is not -1 (or the default value), then there was a partition where each of the slices were in the
# dictionary set.  Using the cache, the string partitions are then found working backwards from the last value in the
# cache; that is, each slices length (as can be found in the cache) is used to compute the current slices start index.
# When the index has been traced all the way back to the beginning of the string, the results (or list of string
# partitions/slices) are returned.
#
# Example:
#   name: amanaplanacanal
#   dictionary_set: {'plan', 'canal', 'bed', 'and', 'a', 'beyond', 'man', 'hand', 'bath', 'bat'}
#
#   The states of last_length:
#                      0   1   2   3   4   5   6   7   8   9  10  11  12  13  14    (Indices)
#                      a   m   a   n   a   p   l   a   n   a   c   a   n   a   l    (String Chars)
#       INITIAL:     [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

#             i:  0  [ 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]   a
#             i:  1  [ 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]   am
#             i:  2  [ 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]   ama
#             i:  3  [ 1, -1, -1,  3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]   aman
#             i:  4  [ 1, -1, -1,  3,  1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]   amana
#             i:  5  [ 1, -1, -1,  3,  1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]   amanap
#             i:  6  [ 1, -1, -1,  3,  1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]   amanapl
#             i:  7  [ 1, -1, -1,  3,  1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]   amanapla
#             i:  8  [ 1, -1, -1,  3,  1, -1, -1, -1,  4, -1, -1, -1, -1, -1, -1]   amanaplan
#             i:  9  [ 1, -1, -1,  3,  1, -1, -1, -1,  4,  1, -1, -1, -1, -1, -1]   amanaplana
#             i: 10  [ 1, -1, -1,  3,  1, -1, -1, -1,  4,  1, -1, -1, -1, -1, -1]   amanaplanac
#             i: 11  [ 1, -1, -1,  3,  1, -1, -1, -1,  4,  1, -1, -1, -1, -1, -1]   amanaplanaca
#             i: 12  [ 1, -1, -1,  3,  1, -1, -1, -1,  4,  1, -1, -1, -1, -1, -1]   amanaplanacan
#             i: 13  [ 1, -1, -1,  3,  1, -1, -1, -1,  4,  1, -1, -1, -1, -1, -1]   amanaplanacana
#             i: 14  [ 1, -1, -1,  3,  1, -1, -1, -1,  4,  1, -1, -1, -1, -1,  5]   amanaplanacanal

#         FINAL:     [1,  -1, -1,  3,  1, -1, -1, -1,  4,  1, -1, -1, -1, -1,  5]
#
# Time Complexity: O(n**2), where n is the length of the string.
# Space Complexity: O(n), where n is the length of the string.
def decompose_into_dictionary_set_memo(string, dictionary_set):
    last_length = [-1] * len(string)
    for i in range(len(string)):                # For each string slice starting from the beginning:
        if string[:i + 1] in dictionary_set:        # If it's in the dictionary:
            last_length[i] = i + 1                      # Mark it's length.
        if last_length[i] == -1:                    # If it's not in the dictionary, try and find a string ending at i
            for j in range(i):                          # starting at j that IS in the dictionary.
                if last_length[j] != -1 and string[j + 1: i + 1] in dictionary_set:     # (string[j+1:i+1] is in dict)
                    last_length[i] = i - j                  # Mark the length of the 'connecting' (smaller) word.
                    break                                   # Break because we only need ONE string partition.
    if last_length[-1] != -1:                   # If there exists a partition with all strings in the dict:
        result = []                                 # This will contain the partitions (all in the dict) of string.
        idx = len(string) - 1                       # Start at the end index.
        while idx >= 0:                                 # while the index is non-negative:
            start = idx + 1 - last_length[idx]              # Compute the start index, then add the slice to result.
            result.insert(0, string[start: start + last_length[idx]])
            idx -= last_length[idx]                         # Update the index.
        return result                               # Return the result


dictionary_set = {"a", "and", "bat", "bath", "bed", "beyond", "canal", "hand", "man", "plan"}
names = ["amanaplanacanal", "bedbathandbeyond", "google"]
fns = [decompose_into_dictionary_set_via_bf,
       decompose_into_dictionary_set_rec,
       decompose_into_dictionary_set_memo]

for name in names:
    print(f"\nname: {name}\ndictionary_set: {dictionary_set}")
    for fn in fns:
        print(f"{fn.__name__}(name, dictionary_set): {fn(name, dictionary_set)}")
    print()


