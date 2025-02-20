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


class NestedDictTrie:
    def __init__(self, *args, word_flag="##"):
        if all(isinstance(arg, str) for arg in args) and word_flag is not None and isinstance(word_flag, str) and len(word_flag) > 1:
            self._root = {}
            self._size = 0
            self._word_flag = word_flag
            for arg in args:
                self.add_word(arg)
            return
        raise TypeError

    def add_word(self, word):
        if word is None or not isinstance(word, str):
            raise TypeError
        n = self._root
        for c in word:
            if c not in n:
                n[c] = {}
            n = n[c]
        if self._word_flag not in n:
            self._size += 1
            n[self._word_flag] = self._word_flag
        return word

    def has_word(self, word):
        if word is None or not isinstance(word, str):
            raise TypeError
        n = self._root
        for c in word:
            if c not in n:
                return False
            n = n[c]
        return self._word_flag in n

    def has_prefix(self, prefix):
        if prefix is None or not isinstance(prefix, str):
            raise TypeError
        n = self._root
        for c in prefix:
            if c not in n:
                return False
        return True

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def get_prefixed_words(self, prefix):
        def _rec(n, acc):
            for k in n:
                if k is self._word_flag:
                    result.append("".join(acc))
                elif len(k) == 1:
                    _rec(n[k], acc + [k])
        if prefix is None or not isinstance(prefix, str):
            raise TypeError
        result = []
        n = self._root
        for c in prefix:
            if c not in n:
                return result
            n = n[c]
        _rec(n, list(prefix))
        return result

    def get_all_words(self):
        return self.get_prefixed_words("")

    def remove_word(self, word):
        def _rec(i, n):
            if i == len(word):
                if self._word_flag not in n:
                    raise KeyError(word)
                else:
                    del n[self._word_flag]
            else:
                _rec(i+1, n[word[i]])
                if len(n[word[i]]) == 0:
                    del n[word[i]]
        if word is None or not isinstance(word, str):
            raise TypeError
        n = self._root
        _rec(0, n)
        return word

    def prune_prefix(self, prefix):
        def _rec(i, n):
            if i == len(prefix)-1:
                if prefix[i] not in n:
                    raise KeyError(prefix)
                else:
                    del n[prefix[i]]
            else:
                if prefix[i] not in n:
                    raise KeyError(prefix)
                _rec(i+1, n[prefix[i]])
        if prefix is None or not isinstance(prefix, str):
            raise TypeError
        n = self._root
        _rec(0, n)
        return prefix

    def __repr__(self):
        return f"{self._root!r}"



print("\nAPPROACH: Via Nested Dictionaries")

arg_list = ("dad", "dads", "daddy", "daddies", "baba")
my_trie = NestedDictTrie(*arg_list)

print("my_trie.get_all_words(): ", my_trie.get_all_words())
print("my_trie.get_prefixed_words(\"da\"): ", my_trie.get_prefixed_words("da"))
print(my_trie)

add_list = ("d", "dan", "dang")
for word in add_list:
    print("my_trie.add_word(" + word + "): ", my_trie.add_word(word))
print(my_trie.get_all_words())
print(my_trie)

del_list = ("daddy", "d", "daddies")
for word in del_list:
    print("my_trie.remove_word(" + word + "): ", my_trie.remove_word(word))
print(my_trie.get_all_words())
print(my_trie)

print("my_trie.has_word(\"dad\"): ", my_trie.has_word("dad"))
print("my_trie.has_word(\"pad\"): ", my_trie.has_word("pad"))
print("my_trie.has_prefix(\"d\"): ", my_trie.has_prefix("dad"))
print("my_trie.has_prefix(\"a\"): ", my_trie.has_prefix("pad"))
print()


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

print("\nAPPROACH: Via Trie Node Object")
root = TrieNode('*')
add(root, "hackathon")
add(root, 'hack')

print(find_prefix(root, 'hac'))
print(find_prefix(root, 'hack'))
print(find_prefix(root, 'hackathon'))
print(find_prefix(root, 'ha'))
print(find_prefix(root, 'hammer'))


