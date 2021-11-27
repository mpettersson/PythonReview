"""
    GENERALIZED ABBREVIATIONS (leetcode.com/problems/generalized-abbreviation)

    Write a function, which accepts a string (word) then returns a list of all generalized abbreviations of the string;
    where a generalized abbreviation of a string can be constructed via replacing any combination of non-overlapping
    substrings with their respective substring lengths.

    Example:
        Input = "word"
        Output = ["4", "3d", "2r1", "2rd", "1o2", "1o1d", "1or1", "1ord", "w3", "w2d", "w1r1", "w1rd", "wo2", "wo1d",
                  "wor1", "word"]

"""
from functools import cache
import time


# APPROACH: Recursion/Backtracking
#
# This approach uses recursion with backtracking to find the abbreviations.  There are 2**n abbreviations for a word of
# length n, since each character can either be abbreviated or not.  It may help to view the recursion tree as a binary
# tree; consider the example where the word is "word":
#
#                                                       "word"
#                                                     /        \
#                       Index=1                   "1ord"      "word"
#                                                 /    \      /    \
#                       Index=2                "2rd"   ...  ...   "word"
#                                              /   \              /    \
#                       Index=3             "3d"   ...          ...   "word"
#                                          /    \                     /    \
#                       Index=4          "4"   "3d"               "wor1"  "word"
#
# In the tree above, the left path inserts numbers, the right path inserts characters, and each leaf node is a member of
# the result list.
#
# NOTE: If you are still lost, try thinking of it like this:
#                                                        word
#                                              ⟋                    ⟍
#                                           ⟋                          ⟍
#  Index=1                       1ord                                            word
#                            /          \                                    /          \
#                           /            \                                  /            \
#  Index=2            11rd                  1ord                     w1rd                    word
#                   /      \              /       \               /        \              /        \
#                  /        \            /         \             /          \            /          \
#  Index=3      111d       11rd        1o1d       1ord         w11d        w1rd        wo1d        word
#              /  \        /  \        /  \        /  \        /  \        /  \        /  \        /  \
#             /    \      /    \      /    \      /    \      /    \      /    \      /    \      /    \
#  Index=4  1111  111d  11r1  11rd  1o11  1o1d  1or1  1ord  w111  w11d  w1r1  w1rd  wo11  wo1d  wor1  word
#
# However, the values would be summed:
# ['4', '3d', '2r1', '2rd', '1o2', '1o1d', '1or1', '1ord', 'w3', 'w2d', 'w1r1', 'w1rd', 'wo2', 'wo1d', 'wor1', 'word']
#
# Time complexity: O(n *(2**n)), where n is the length of the string.  The is due to the recursion tree's 2**n leaves,
#                  where each leaf must build a string in O(n) time. (The 2**n-1 inner nodes are all constant time).
# Space Complexity: O(n * (2**n)), where n is the length of the string (O(n) if the result list is ignored).
def generate_abbreviations_rec(word):

    def _rec(i, n, acc):
        if i == len(word):
            result.append(acc + str(n) if n > 0 else acc)           # Once at end, append current to the result
        else:
            _rec(i+1, n+1, acc)                                         # Skip current position, and increment count
            _rec(i+1, 0, acc + (str(n) if n > 0 else '') + word[i])     # Include curr position & zero-out count

    result = []
    _rec(0, 0, '')
    return result


# APPROACH: Recursion/Backtracking Alternate
#
# This approach is yet another recursive backtracking solution.
#
# Time complexity: O(n * (2**n)), where n is the length of the string.
# Space Complexity: O(n * (2**n)), where n is the length of the string (O(n) if the result list is ignored).
def generate_abbreviations_rec_alt_0(word):

    def _dfs(abbr, index, r):
        r.append(abbr)
        for s in range(1, len(abbr)+1):
            for i in range(index, len(abbr)):
                if len(abbr) - i >= s:
                    _dfs(abbr[:i]+str(s)+abbr[i+s:], i+len(str(s))+1, r)

    res = []
    _dfs(word, 0, res)
    return res


# APPROACH: Recursion/Backtracking Alternate
#
# This approach is yet another recursive backtracking solution.
#
# Time complexity: O(n * (2**n)), where n is the length of the string.
# Space Complexity: O(n * (2**n)), where n is the length of the string (O(n) if the result list is ignored).
def generate_abbreviations_rec_alt_1(word):

    def _rec(word, i, n, acc, result):
        if i == len(word):                          # If index i is at end:
            if n:                                       # If we need to append the current count to the end:
                acc.append(str(n))                          # Append the count to the accumulator.
            result.append("".join(acc))                 # Add the accumulated word to the result list.
            return
        _rec(word, i+1, n+1, acc, result)           # RECURSE with index+1, count+1, and SAME accumulator.
        acc.pop()                                   # This ALWAYS removes a COUNT that was added to the accumulator.
        if n:
            acc.append(str(n))
        _rec(word, i+1, 0, acc+[word[i]], result)   # RECURSE with index+1, COUNT RESET, and accumulator + [word[i]].

    result = []
    _rec(word, 0, 0, [], result)
    return result


# APPROACH: Recursion/Backtracking Alternate
#
# This approach is yet another recursive backtracking solution.
#
# Time complexity: O(n * (2**n)), where n is the length of the string.
# Space Complexity: O(n * (2**n)), where n is the length of the string (O(n) if the result list is ignored).
def generate_abbreviations_rec_alt_2(word):

    def _dfs(s, acc):
        if not s:                                       # If s is empty:
            result.append(acc)                              # Add the accumulated string.
            return
        for i in range(len(s)+1):                       # For COUNT in range len(s) to len(word)+1:
            if i == 0:                                      # If the count is zero:
                _dfs(s[1:], acc + s[i])                         # Just continue with:  s[1:] and the accumulator + s[i]
            else:                                           # Else, if there is a count:
                _dfs(s[i+1:], acc + str(i) + s[i:i+1])          # Continue with the inserted number and next letter.

    result = []
    _dfs(word, '')
    return result


# APPROACH: Bit Manipulation
#
# This approach maps binary 1s/0s to abbreviated/non-abbreviated characters (in the word) to generate all abbreviations.
#
# This is done by iterating over all numbers from from 0 to 2**(len(word))-1.  Each of the numbers binary digits are
# used according to the following rules; if the bit is set (or has a value of 1), the corresponding character is
# abbreviated, if the bit is unset (or has a value of 0), the corresponding character is not abbreviated.
#
# For example, using this encoding, a given string of "word" and the number 0b0011 would produce the result "wo2";
# that is, because the first two bits are not set the characters are kept, whereas the last two bits are set so they
# (the last two characters) are abbreviated.
#
# Time Complexity: O(n * (2**n)). Building one abbreviation from the number x, we need scan all the n bits.
# Space Complexity: O(n * (2**n)), where n is the length of the string (O(n) if the result list is ignored).
def generate_abbreviations_bit_mask(word):

    def _abbreviate(word, x):           # build the abbreviation for word from number x
        acc = []
        k = 0                           # k = the count of consecutive ones in x
        n = len(word)
        i = 0
        while i < n:
            if (x & 1) == 0:            # The bit is zero, so, keep the character
                if k != 0:              # we have abbreviated k characters
                    acc.append(str(k))
                    k = 0               # reset the counter
                acc.append(word[i])
            else:                       # bit is one, increase k
                k += 1
            i += 1
            x >>= 1
        if k != 0:                      # don't forget to append the last k if non zero
            acc.append(str(k))
        return ''.join(acc)

    ans = []
    x = 0
    while x < (1 << len(word)):         # While x < 2**len(word)
        ans.append(_abbreviate(word, x))
        x += 1
    return ans


# APPROACH: Memoization/Top Down Dynamic Programming
#
# This approach breaks a single recursive (nested) function into two (nested) functions; one for character abbreviations
# and one for number abbreviations.  This clear division allows for caching the function calls via functools lru_cache.
#
# Time Complexity: O(n * (2**n)). Building one abbreviation from the number x, we need scan all the n bits.
# Space Complexity: O(n * (2**n)), where n is the length of the string (O(n) if the result list is ignored).
def generate_abbreviations_top_down(word):

    @cache
    def dp_last_letter_only(n):
        if n == 1:
            return [word[0]]
        so_far = []
        c = word[n-1]
        so_far.extend((x+c for x in dp_last_letter_only(n-1)))
        so_far.extend((x+c for x in dp_last_number_only(n-1)))
        return so_far

    @cache
    def dp_last_number_only(n):
        if n == 1:
            return ["1"]
        so_far = [str(n)]
        for k in range(1, n):
            s = str(n - k)
            x = dp_last_letter_only(k)
            so_far.extend(a+s for a in dp_last_letter_only(k))
        return so_far

    if isinstance(word, str):
        n = len(word)
        if n == 0:
            return ['']
        return dp_last_number_only(n) + dp_last_letter_only(n)


# APPROACH: Tabulation/Bottom Up Dynamic Programming
#
# This approach uses two tabulation/memoization tables, or caches, to incrementally build all of the abbreviations.
# There is a list of lists for number abbreviations (which is filled out first) and a list of lists for the character
# abbreviations (which is filled out after the number abbreviations) for each combination of character lengths (starting
# at the end of the word and working towards the beginning). Once both lists of lists have been populated, the first
# row (or the row with a character count equal to the length of the original word), of both lists of list, are returned
# (concatenated together) as the list of abbreviations.
#
# Time Complexity: O(n * (2**n)). Building one abbreviation from the number x, we need scan all the n bits.
# Space Complexity: O(n * (2**n)), where n is the length of the string (O(n) if the result list is ignored).
def generate_abbreviations_bottom_up(word):
    if isinstance(word, str):
        n = len(word)
        if n == 0:
            return ['']
        num_abbrs = [[] for _ in range(n)]      # Contains cached num/char abbreviations; where index [-1] has only
        char_abbrs = [[] for _ in range(n)]     # 1 char, index [-2] has 2 char combos, index [-3] has 3 char combos
        num_abbrs[-1] = ['1']                   # etc.  This, and the reverse range iteration (below) are so that we
        char_abbrs[-1] = [word[-1]]             # can work to a single number total (i.e., "word" => abbr "4").

        for i in range(n-2, -1, -1):            # Work backwards, start at second to last, go to first...

            for j in range(1, n-i):                 # This section updates num_abbrs[i]; it ONLY copies from
                for s in char_abbrs[i+j]:               # char_abbrs[i+j] (but prepends j's value in front).
                    num_abbrs[i].append(f'{j}{s}')
            num_abbrs[i].append(f'{n-i}')           # And adds n-i (to num_abbrs[i]).

            for s in num_abbrs[i+1]:                # This section updates char_abbrs[i]; by copying from BOTH
                char_abbrs[i].append(f'{word[i]}{s}')   # (the previous) num_abbrs[i+1] AND
            for s in char_abbrs[i+1]:
                char_abbrs[i].append(f'{word[i]}{s}')   # it's previous abbreviations (char_abbrs[i+1]).

        return num_abbrs[0] + char_abbrs[0]


args = ['word',
        'a',
        'abcde',
        'aaaaa',
        '']
fns = [generate_abbreviations_rec,
       generate_abbreviations_rec_alt_0,
       generate_abbreviations_rec_alt_1,
       generate_abbreviations_rec_alt_2,
       generate_abbreviations_bit_mask,
       generate_abbreviations_top_down,
       generate_abbreviations_bottom_up]

for s in args:
    for fn in fns:
        print(f"{fn.__name__}({s!r}): {fn(s)}")
    print()

s = "mpettersson"
print(f"s: {s!r}")
for fn in fns:
    t = time.time()
    print(f"{fn.__name__}(s) took ", end="")
    fn(s)
    print(f"{time.time() - t} seconds.")
print()


