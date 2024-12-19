"""
    NUM DELETIONS (50CIQ 46: STRING DELETION,
                   leetcode.com/problems/longest-word-in-dictionary-through-deleting)

    Write a function, which accepts a string and a dictionary set of strings, and returns the minimum number of
    character deletions (from the string) to make a word in the dictionary set.

    Example:
        Input = "abc", {"a", "aa", "aaa"}
        Output = 2

    Variations:
        - Return the longest word in the dictionary that can be achieved via deletions of the string.
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What type is the dictionary?
#   - Are we asking this once or many times (might want to do preprocessing if many calls on dict)?
#   - Can you add characters (although the description already pretty clear)?
#   - What should happen if a word in the dictionary can't be made?
#   - Capitalization?


# APPROACH: BFS
#
# Execute a BFS on the string, where the children/adjacent nodes are the strings that can be created from deleting a
# single character from the current string. Once a match is found return the difference of the original string length
# and the matching strings length.
#
# Using the example above, where the string is "abc" and the dictionary is {"a", "aa", "aaa"}, the following tree
# represents the BFS search string order:
#
#             abc
#         ⟋   ｜    ⟍
#       ab     ac     bc
#     ⟋ ⟍    ⟋ ⟍    ⟋ ⟍
#    a    b  a   c   b   c
#
# Time Complexity: O(n!), where n is the length of the string.
# Space Complexity: O(n!), where n is the length of the string.
def num_deletions_bfs(string, dictionary_set):
    if string and dictionary_set:
        queue = [string]
        seen_set = set()                        # Prevent checking duplicates (small optimization).
        while queue:
            s = queue.pop(0)                    # s is string with one or more deletions.
            if s in dictionary_set:
                return len(string) - len(s)
#               return s                        # ALTERNATE QUESTION: Find longest WORD in dict (not num of deletions).
            for i in range(len(s)):
                temp = s[:i] + s[i+1:]
                if temp not in seen_set:
                    queue.append(temp)
                    seen_set.add(temp)
    return -1
#   return ""                                   # ALTERNATE QUESTION: Find longest WORD in dict (not num of deletions).


# APPROACH: Sort With Two Pointers
#
# This approach first sorts the dictionary by length (descending) and lexicographical (ascending) order; this guarantees
# that the first match has the minimum number of deletions.  Then, the string is compared to each of the words in the
# dictionary set via two pointers.  The pointer in the string may be advanced without a match (if a deletion occurs),
# however, the word pointer must match a character in the string before being advanced.  If the word pointer reaches the
# end of the word then a full mach has occurred and the difference in lengths is returned as the number of deletions.
#
# Time Complexity: O((s * w) + (w * log(w))), which reduces to O(w * (s + log(w))), where w and s are the length of the
#                  string and the total size of the words dictionary.
# Space Complexity: O(w), where w is the total size of the words dictionary (if dictionary set was provided as a list,
#                   then it could be sorted in place, and the space would just be O(s) for the return string.
def num_deletions_sort(string, dictionary_set):
    if string and dictionary_set:
        if string in dictionary_set:                # Feelin lucky?
            return string
        for word in sorted(dictionary_set, key=lambda x: (-len(x), x)):  # Sort by len descending, and word ascending.
            s_len = len(string)
            w_len = len(word)
            if s_len > w_len:                       # Since s not in dict, s must be longer to facilitate deletions.
                i = j = 0                           # i is the current index in s, j is current index in word
                while i < s_len and j < w_len:
                    if string[i] == word[j]:        # A char in s matches a char in word, increment to next char in word
                        j += 1
                    i += 1                          # Try next char in s (that is, would need to delete this char).
                if j == w_len:                      # s was able to match all of the characters in word.
                    return s_len - w_len            # Return the number of deletions
#                   return word                 # ALTERNATE QUESTION: Find longest WORD in dict (not num of deletions).
    return -1
#   return ""                                   # ALTERNATE QUESTION: Find longest WORD in dict (not num of deletions).


# APPROACH: Two Pointers
#
# This approach is similar to the sorting approach above in that the provided string is compared (via two pointers) to
# words in the dictionary (one at a time).  As opposed to sorting, this approach maintains the longest word (via
# deletions), and whenever a new match is found, updates longest (if needed).  After all words have been compared, the
# difference of the lengths is returned.
#
# Time Complexity: O(s * w), where s and w are the length of the string and the number of words in the dictionary set.
# Space Complexity: O(s), where s is the length of the string.
def num_deletions(string, dictionary_set):
    if string and dictionary_set:
        longest = ""
        for word in dictionary_set:
            w_len = len(word)
            i = 0                                   # i is the word index pointer.
            for c in string:
                if i < w_len and c == word[i]:      # If pointer and character match
                    i += 1
                if i == w_len:                      # If all of the word matches characters in string:
                    if w_len > len(longest) or (w_len >= len(longest) and word < longest):  # And the word is longer
                        longest = word              # Update longest.
        return -1 if longest == "" else len(string) - len(longest)
#       return longest                          # ALTERNATE QUESTION: Find longest WORD in dict (not num of deletions).
    return -1
#   return ""                                   # ALTERNATE QUESTION: Find longest WORD in dict (not num of deletions).


dict_set = {'a', 'aa', 'aaa', 'acre', 'admirer', 'algorithmic', 'and', 'angered', 'axe', 'bat', 'bath', 'bed', 'beyond',
            'bite', 'canal', 'care', 'creative', 'death', 'dog', 'elvis', 'enraged', 'fights', 'flea', 'fun',
            'funeral', 'god', 'hand', 'hated', 'ipsum', 'leaf', 'levis', 'listens', 'lives', 'logarithmic', 'lorem',
            'man', 'married', 'metal', 'money', 'my', 'plan', 'race', 'reactive', 'shiny', 'silent', 'they'}
strings = ["abc", "mario", "battery", "hello world", "", None]
fns = [num_deletions_bfs,
       num_deletions_sort,
       num_deletions]

print(f"dict_set: {dict_set}\n")
for string in strings:
    for fn in fns:
        print(f"{fn.__name__}({string!r}, dict_set): {fn(string, dict_set)}")
    print()


