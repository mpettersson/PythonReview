"""
    MULTI SEARCH

    Given a string b and a array of smaller strings T, design a method to search b for each small string in T.

    Example
        Input:  b = "mississippi"
                T = ["is", "ppi", "hi", "sis", "i", "ssippi"]
"""


# Approach 1: Brute Force; runtime is O(kbt), where k is the length of the longest string in T, b is the length of the
# bigger string, and t is the number of smaller strings within T.
def multi_search_brute_force(s, l):
    lookup = dict()
    for small in l:
        lookup[small] = brute_force_search(s, small)
    return lookup


def brute_force_search(big, small):
    locations = []
    for i in range(len(big) - len(small) + 1):
        if is_substring_at_location(big, small, i):
            locations.append(i)
    return locations


def is_substring_at_location(big, small, offset):
    for i in range(len(small)):
        if big[offset + i] != small[i]:
            return False
    return True


# Solution 2: Trie with all suffixes of big string, runtime is O(b**2) to create the tree and O(kt) to search, where
# k is the length of the longest string in T, b is the length of the big string and t is the number of strings in T.
# NOTE: If b is very large, then Solution 1 with O(bkt) is better.  If len(T) is large, then this solution with a
# runtime of O(b**2 + kt) might be better (than Solution 1).
def multi_search_suffixes_trie(big, smalls):
    lookup = dict()
    tree = create_trie_from_string(big)
    for s in smalls:
        locations = tree.search(s)
        subtract_value(locations, len(s))
        lookup[s] = locations
    return lookup


def create_trie_from_string(s):
    trie = Trie()
    for i in range(len(s)):
        trie.insert_string(s[i:], i)
    return trie


def subtract_value(locations, delta):
    if locations is None:
        return
    for i in range(len(locations)):
        locations[i] = locations[i] - delta


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.indexes = list()
        self.value = None

    def insert_string(self, s, index):
        self.indexes.append(index)
        if s is not None and len(s) > 0:
            self.value = s[0]
            child = None
            if self.value in self.children:
                child = self.children[self.value]
            else:
                child = TrieNode()
                self.children[self.value] = child
            remainder = s[1:]
            child.insert_string(remainder, index + 1)
        else:
            self.children['\0'] = None

    def search(self, s):
        if s is None or len(s) == 0:
            return self.indexes
        else:
            first = s[0]
            if first in self.children:
                return self.children[first].search(s[1:])
        return None

    def terminates(self):
        return '\0' in self.children

    def get_child(self, c):
        if c in self.children:
            return self.children[c]
        else:
            return None


class Trie:
    def __init__(self, s=None):
        self.root = TrieNode()
        if s is not None:
            self.insert_string(s, 0)

    def search(self, s):
        return self.root.search(s)

    def insert_string(self, s, location):
        self.root.insert_string(s, location)

    def get_root(self):
        return self.root


# Solution 3: Optimal--Trie of smaller strings; the runtime is O(kt) to create the tire and O(bk) to search where k is
# the length of the longest string in T, b is the length of the big string and t is the number of strings in T.
# O(kt + bk) is better than Solution 1's O(kbt) and since b is always larger than k (the longest string in T) it is also
# better than Solution 2's O(b**2 + kt) time.
def multi_search_trie(big, smalls):
    lookup = dict()
    max_len = len(big)
    root = create_tree_from_string_list(smalls, max_len).get_root()
    for i in range(len(big)):
        strings = find_strings_at_loc(root, big, i)
        insert_into_dict(strings, lookup, i)
    return lookup


def insert_into_dict(strings, d, index):
    for s in strings:
        if s in d:
            d[s].append(index)
        else:
            d[s] = [index]


def create_tree_from_string_list(smalls, max_len):
    tree = Trie("")
    for s in smalls:
        if len(s) <= max_len:
            tree.insert_string(s, 0)
    return tree


def find_strings_at_loc(root, big, start):
    strings = []
    index = start
    while index < len(big):
        root = root.get_child(big[index])
        if root is None:
            break
        if root.terminates():
            strings.append(big[start:index + 1])
        index += 1
    return strings


string = "mississippi"
little_string_list = ["is", "ppi", "hi", "sis", "i", "ssippi"]
print("string:", string)
print("little_string_list:", little_string_list)
print()

print("sorted(multi_search_brute_force(string, little_string_list).items()):",
      sorted(multi_search_brute_force(string, little_string_list).items()))

print("sorted(multi_search_suffixes_trie(string, little_string_list).items()):",
      sorted(multi_search_suffixes_trie(string, little_string_list).items()))

print("sorted(multi_search_trie(string, little_string_list).items()):",
      sorted(multi_search_trie(string, little_string_list).items()))


