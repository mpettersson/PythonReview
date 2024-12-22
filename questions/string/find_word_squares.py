"""
    FIND WORD SQUARES (leetcode.com/problems/word-squares)

    Given a set of words (without duplicates), find all word squares you can build from them.

    A sequence of words forms a valid word square if the kth row and column read the exact same string, where
    0 ≤ k < max(numRows, numColumns).

    Consider the following word square:
        b a l l
        a r e a
        l e a d
        l a d y

    The above is a word square because each word reads the same both horizontally and vertically.

    Example:
        Input = ['area', 'lead', 'wall', 'lady', 'ball']
        Output = [['wall', 'area', 'lead', 'lady'], ['ball', 'area', 'lead', 'lady']]

            Or:
                b a l l     w a l l
                a r e a     a r e a
                l e a d     l e a d
                l a d y     l a d y

"""
import time


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - What are the possible characters?
#   - What are the possible list lengths?
#   - What are the possible string lengths (empty string)?


# APPROACH:
#
#
#
# Time Complexity: O(n * 26**(l**2))
# Space Complexity: O(~n * l + l * 1/2) = O(n * l)

# SEE: https://www.goodtecher.com/leetcode-425-word-squares/
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word_list = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.word_list.append(word)
        node.is_word = True

    def find(self, word):
        node = self.root
        for char in word:
            node = node.children.get(char)
            if node is None:
                return None
        return node

    def word_prefix(self, prefix):
        node = self.find(prefix)
        return [] if node is None else node.word_list


def find_word_squares(words):

    def _search(trie, square, results):
        n, pos = len(square[0]), len(square)
        if pos == n:
            results.append(list(square))
            return
        for col in range(pos, n):
            prefix = ''.join(square[i][col] for i in range(pos))
            if trie.find(prefix) is None:
                return
        prefix = ''.join(square[i][pos] for i in range(pos))
        for word in trie.word_prefix(prefix):
            square.append(word)
            _search(trie, square, results)
            square.pop()

    trie = Trie()
    for word in words:
        trie.add(word)
    results = []
    for word in words:
        _search(trie, [word], results)
    return results



def format_matrix(m):
    try:
        w = max([len(str(e)) for r in m for e in r]) + 1
    except (ValueError, TypeError):
        return f"\n{None}"
    return m if not m else '\t' + '\n\t'.join([''.join([f'{e!r:{w}}' for e in r if len(r) > 0]) for r in m if len(m) > 0])


args = [["area", "lead", "wall", "lady", "ball"],
        ["abat", "baba", "atan", "atal"]]
fns = [find_word_squares]

for l in args:
    print(f"l: {l!r}")
    for fn in fns:
        print(f"{fn.__name__}(s): {fn(l)!r}")
    print()
