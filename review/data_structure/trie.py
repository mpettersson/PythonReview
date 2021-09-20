"""
    TRIE (AKA PREFIX TREE, AKA DIGITAL TREE)

    TODO:
        - Add more functionality (only add and basic searches are available now).
        - Add and improve the examples.

    A trie is a type of SEARCH TREE, a tree data structure used for locating specific keys from within a set. These keys
    are most often strings, with links between nodes defined not by the entire key, but by individual characters. In
    order to access a key (to recover its value, change it, or remove it), the trie is traversed depth-first, following
    the links between nodes, which represent each character in the key.

    All the children of a node have a common prefix of the string associated with that parent node, and the root is
    associated with the empty string. Nodes in a trie do not (usually) store their associated key; a node's position in
    the trie defines the key with which it is associated. This distributes the value of each key across the data
    structure, and means that not  every node necessarily has an associated value.

    The idea of a trie for representing a set of strings was first abstractly described by Axel Thue in 1912. Tries were
    first described in a computer context by René de la Briandais in 1959. The idea was independently described in 1960
    by Edward Fredkin, who coined the term trie, pronouncing it 'tri' (as "tree"), after the middle syllable of
    reTRIeval. However, other authors pronounce it 'traɪ' (as "try"), in an attempt to distinguish it verbally from
    "tree".

    NOTE: Several basic implementations are included below, however, trie packages are also available:
            - pypi.python.org/pypi/marisa-trie/ - C++ based implementation.
            - github.com/bdimmick/python-trie   - Pure python, simple implementation.
            - pypi.python.org/pypi/PyTrie       - Pure python, more complex implementation.
            - github.com/google/pygtrie         - Pure python, Google implementation.
            - pypi.org/project/datrie/          - Double array trie implementation based on libdatrie.

    References:
        - wikipedia.org/wiki/Trie
        - stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python
"""


# APPROACH: Via Nested Dictionaries
#
# This approach uses nested dictionaries as a trie.  This is a simple, easy to understand implementation, however, for
# a large (or scalable) trie, it may be space inefficient.
#
# SEE: https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python#answer-30124562
#      https://leetcode.com/problems/implement-trie-prefix-tree/discuss/1426130/Python-3-or-simple-trie-using-dictionary
class NestedDictionariesTrie:

    def __init__(self):
        """Initialize your data structure here."""
        self.trie = {}

    def add(self, word: str) -> None:
        """Adds a word into the trie."""
        t = self.trie
        for ch in word:
            if ch not in t:
                t[ch] = {}
            t = t[ch]

        t['#'] = '#'

    def search(self, word: str) -> bool:
        """Returns True if the word is in the trie False otherwise."""
        t = self.trie
        for ch in word:
            if ch not in t:
                return False
            t = t[ch]
        if '#' in t:
            return True
        return False

    def has_prefix(self, prefix: str) -> bool:
        """Returns True if there is any word in the trie that starts with the given prefix."""
        t = self.trie
        for ch in prefix:
            if ch not in t:
                return False
            t = t[ch]
        return True


obj = NestedDictionariesTrie()
obj.add("python")
param_2 = obj.search("python")
param_3 = obj.startsWith("py")


# APPROACH: Via Trie Node Object
#
# This approach uses a more traditional node class as the underlining data structure, which is more customizable (but
# also more space inefficient).
class TrieNode(object):
    """A basic trie node implementation."""

    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False          # Is it the last character of the word.
        self.counter = 1                    # How many times this character appeared in the addition process


def add(root, word: str):
    """Adding a word in the trie structure"""
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:         # Search for the character in the children of the present `node`
            if child.char == char:
                child.counter += 1          # Increment counter; to keep track that another word has it as well
                node = child                # And point the node to the child that contains this char
                found_in_child = True
                break
        if not found_in_child:              # Not found; add a new child.
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node                 # And then point node to the new child
    node.word_finished = True               # Everything finished. Mark it as the end of a word.


def find_prefix(root, prefix: str):
    """Check and return
        1. If the prefix exists in any of the words we added so far
        2. If yes then how may words actually have the prefix"""
    node = root
    if not root.children:                   # If the root node has no children (EMPTY trie), then return False.
        return False, 0
    for char in prefix:
        char_not_found = True
        for child in node.children:         # Search through all the children of the present `node`
            if child.char == char:          # We found the char existing in the child.
                char_not_found = False
                node = child                # Assign node as the child containing the char and break
                break
        if char_not_found:
            return False, 0                 # Return False anyway when we did not find a char.
    return True, node.counter               # Found the prefix: return True and number of words the prefix has.


root = TrieNode('*')
add(root, "hackathon")
add(root, 'hack')

print(find_prefix(root, 'hac'))
print(find_prefix(root, 'hack'))
print(find_prefix(root, 'hackathon'))
print(find_prefix(root, 'ha'))
print(find_prefix(root, 'hammer'))


