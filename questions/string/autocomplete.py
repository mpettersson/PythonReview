"""
    AUTOCOMPLETE (50CIQ 45: AUTOCOMPLETE)

    Implement autocomplete functionality; that is, given a list of strings and a prefix string, return a list of all
    words (from the provided list) with the provided prefix.

    Example:
        Input = ['abc', 'acd', 'bcd', 'def', 'a', 'aba'], 'a'
        Output = ['abc', 'acd', 'a', 'aba']

        Input = ['abc', 'acd', 'bcd', 'def', 'a', 'aba'], 'b'
        Output = ['bcd']
"""


# Questions you should ask:
#   - What format will the dictionary be in (file, stream, list, etc.)?
#   - What is the character set?
#   - Capitalization?


# APPROACH: Naive/Brute Force
#
# This approach simply iterates over all strings in the string/word set, checking if the word starts with the provided
# prefix.  If the string does, it is added to a result list.  Once all words have been compared, the result list is
# returned.
#
# Time Complexity:  O(n * p), where n is the number of words in the word set and p is the length of the prefix string.
# Space Complexity:  O(s), where s is the size of the word set.
def autocomplete_via_naive_bf(word_set, prefix):
    if word_set is not None and prefix is not None:
        result = []
        for word in word_set:
            if word.startswith(prefix):
                result.append(word)
        return result


# APPROACH: Trie/Prefix Tree
#
# This approach utilizes the TrieNodesTrie class, which has a single member variable root, which is of type TrieNode.  A
# TrieNode contains a dictionary of children (TrieNodes), as well as a boolean is_word value denoting if the current
# node is the end of a valid word and the nodes prefix, or the concatenation of all of the nodes from root to the node.
#
# Time Complexity:  See below.
# Space Complexity:  See below.
def autocomplete_via_trie_nodes_trie(word_set, prefix):
    trie = TrieNodesTrie(word_set)
    return trie.get_all_words_with_prefix(prefix)


class TrieNode:
    # Time Complexity:  O(1).
    # Space Complexity:  O(p), where p is the size of the prefix.
    def __init__(self, prefix, is_word=False):
        self.prefix = prefix
        self.children = {}
        self.is_word = is_word

    # Time Complexity:  O(1).
    # Space Complexity:  O(1).
    def __str__(self):
        return str(self.prefix)

    # Time Complexity:  O(d), where d is the number of descendants of the node.
    # Space Complexity:  O(d), where d is the number of descendants of the node.
    def __repr__(self):
        return f"prefix:{self.prefix!r}, is_word:{self.is_word}, children:{repr(self.children)}"


class TrieNodesTrie:
    # Time Complexity:  O(u), where u is the set of all possible unique prefixes of all the supplied strings.
    # Space Complexity:  O(u), where u is the set of all possible unique prefixes of all the supplied strings.
    def __init__(self, strings):
        self.root = TrieNode("")
        for s in strings:
            self.insert(s)

    # Time Complexity:  O(n), where n is the length of the word.
    # Space Complexity:  O(n), where n is the length of the word.
    def insert(self, string):
        node = self.root
        for i in range(len(string)):
            node.children.setdefault(string[i], TrieNode(string[:i+1]))
            node = node.children[string[i]]
        node.is_word = True

    # Time Complexity:  O(p), where p is the number of words in the subtree with the root's prefix equal to the prefix.
    # Space Complexity:  O(p), where p is the number of words in the subtree with the root's prefix equal to the prefix.
    def get_all_words_with_prefix(self, prefix):
        if prefix is not None:
            result = []
            node = self.root
            for c in prefix:
                if c in node.children:
                    node = node.children[c]
                else:
                    return result
            queue = [node]
            while queue:
                node = queue.pop(0)
                if node.is_word:
                    result.append(node.prefix)
                for k, v in node.children.items():
                    queue.append(v)
            return result

    # Time Complexity:  O(n), where n is the length of the word.
    # Space Complexity:  O(1).
    def contains_prefix(self, prefix):
        node = self.root
        try:
            for c in prefix:
                node = node.children[c]
            return True
        except KeyError:
            return False

    # Time Complexity:  O(p), where p is the number of words in the subtree with the root's prefix equal to the prefix.
    # Space Complexity:  O(p), where p is the number of words in the subtree with the root's prefix equal to the prefix.
    def __repr__(self):
        return f"Trie.root: {repr(self.root)}"


# APPROACH: Nested Dictionary Trie/Prefix Tree
#
# This approach makes use of a single NestedDictionariesTrie class, the class contains a single member variable (tries),
# which is a dictionary of strings to dictionaries.  Each nested dictionary can only contain one of two keys; a single
# character or a string with the value 'is_word' (which is a boolean value denoting if the current character is an end
# of a valid word).
#
# Time Complexity:  See below.
# Space Complexity:  See below.
def autocomplete_via_nested_dicts_trie(word_set, prefix):
    trie = NestedDictionariesTrie(word_set)
    return trie.get_all_words_with_prefix(prefix)


# A trie wrapper class; contains a single member variable, trie, which is a dictionary of strings to dictionaries.
class NestedDictionariesTrie:

    # Time Complexity:  O(u), where u is the set of all possible unique prefixes of all the supplied strings.
    # Space Complexity:  O(u), where u is the set of all possible unique prefixes of all the supplied strings.
    def __init__(self, word_set):
        self.trie = {}
        for word in word_set:
            self.insert(word)

    # Time Complexity:  O(n), where n is the length of the word.
    # Space Complexity:  O(n), where n is the length of the word.
    def insert(self, word):
        if isinstance(word, str):
            t = self.trie
            for ch in word:
                if ch not in t:
                    t[ch] = {"is_word": False}
                t = t[ch]
            t["is_word"] = True

    # Time Complexity:  O(p), where p is the number of words in the subtree with the root's prefix equal to the prefix.
    # Space Complexity:  O(p), where p is the number of words in the subtree with the root's prefix equal to the prefix.
    def get_all_words_with_prefix(self, prefix):
        def _rec(d, a_l, result):
            if d.get("is_word", False):
                result.append(''.join(a_l))
            for k in d:
                if k != "is_word":
                    a_l.append(k)
                    _rec(d[k], a_l, result)
                    a_l.pop()
        if isinstance(prefix, str):
            t = self.trie
            result = []
            a_l = []
            for ch in prefix:
                if ch in t:
                    t = t[ch]
                    a_l.append(ch)
                else:
                    return result
            _rec(t, a_l, result)
            return result


word_set = {'lorem', 'hand', 'abc', 'lives', 'angered', 'hated', 'aba', 'elvis', 'levis', 'dog', 'canal', 'listens',
            'bcd', 'bat', 'fights', 'axe', 'algorithmic', 'leaf', 'acd', 'funeral', 'a', 'flea', 'my', 'enraged', 'man',
            'metal', 'logarithmic', 'married', 'silent', 'creative', 'care', 'ipsum', 'plan', 'admirer', 'def', 'bath',
            'acre', 'race', 'death', 'god', 'reactive', 'bed', 'aaa', 'aa', 'fun', 'they', 'bite', 'beyond', 'shiny',
            'money', 'and'}
prefix_list = ['a',
               'aa',
               'aaa',
               'b',
               '',
               'z',
               None]
fns = [autocomplete_via_naive_bf,
       autocomplete_via_trie_nodes_trie,
       autocomplete_via_nested_dicts_trie]
print(f"\nword_set: {word_set}\n")

for prefix in prefix_list:
    for fn in fns:
        print(f"{fn.__name__}(word_set, {prefix!r}): {fn(word_set, prefix)}")
    print()


