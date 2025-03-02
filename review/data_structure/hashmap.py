"""
    HASHMAP, HASHTABLE, DICTIONARY, ASSOCIATIVE ARRAY, SYMBOL TABLE

    A hashmap is a data structure that stores key-value pairs, providing an efficient way to retrieve, insert, and
    delete data. It uses a hash function to compute an index (or hash code) into an array, where the value associated
    with a key is stored.

    Key Characteristics of a Hashmap
        - Key-Value Storage: Data is stored in pairs, where each key is unique, and each key maps to a specific value.
        - Hash Function: A function mapping keys to array indices with the goal of uniform distribution across the array.
        - Fast Operations: Lookup, Insertion, and Deletion; These operations are, on average, O(1) (constant time),
          assuming the hash function minimizes collisions.
        - Handling Collisions: If two keys hash to the same index, collisions occur. There are two common strategies to
          resolve collisions include:
            + Chaining: Store multiple key-value pairs at the same index using a linked list or another data structure.
            + Open Addressing: Probe other indices in the array to find an empty slot.

    Time and Space Complexity:
                Average         Worst
        Search: O(1)            O(n)
        Insert: O(1)            O(n)
        Delete: O(1)            O(n)
        Space:  O(n)            O(n)

    Applications:
        - Caching: Store and retrieve frequently used data.
        - Counting Frequencies: Count occurrences of elements (e.g., words in a text).
        - Indexing: Efficiently store and look up data by a unique identifier.
        - Set Implementation: Hashmaps often serve as the backbone for sets.

    History:
        The idea of hashing arose independently in different places. In January 1953, Hans Peter Luhn wrote an internal
        IBM memorandum that used hashing with chaining. The first example of open addressing was proposed by A. D. Linh,
        building on Luhn's memorandum.

    References:
        - en.wikipedia.org/wiki/Hash_table
"""


class HashNode:
    def __init__(self, key, value=None, next_node=None):
        if next_node is not None and not isinstance(next_node, self.__class__):
            raise TypeError
        self.key = key
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return f"{self.key!r}: {self.value!r}"


class HashMap:
    def __init__(self, init_capacity=10, load_capacity=.7):
        self.size = 0
        if init_capacity < 1 or load_capacity <= 0 or load_capacity > 1:
            raise TypeError
        self.capacity = init_capacity
        self.load_capacity = load_capacity
        self._list = [None] * self.capacity

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def get_index(self, key):
        return hash(key) % self.capacity

    def remove(self, key):
        index = self.get_index(key)
        node = self._list[index]
        prev = None
        while node:
            if node.key is key:
                self.size -= 1
                if prev:
                    prev.next_node = node.next_node
                else:
                    self._list[index] = node.next_node
                return node.value
            prev = node
            node = node.next_node
        raise KeyError(key)

    def get(self, key):
        node = self._list[self.get_index(key)]
        while node:
            if node.key is key:
                return node.value
            node = node.next_node
        raise KeyError(key)

    def add(self, key, value):
        index = self.get_index(key)
        node = self._list[index]
        while node:
            if node.key is key:
                node.value = value
                return value
            node = node.next_node
        self.size += 1
        self._list[index] = HashNode(key, value, self._list[index])
        if self.size / self.capacity > self.load_capacity:
            temp = self._list
            self.capacity = self.capacity * 2
            self.size = 0
            self._list = [None] * self.capacity
            for i in temp:
                while i:
                    self.add(i.key, i.value)
                    i = i.next_node
        return value

    def keys(self):
        result = []
        for n in self._list:
            while n:
                result.append(n.key)
                n = n.next_node
        return result

    def values(self):
        result = []
        for n in self._list:
            while n:
                result.append(n.value)
                n = n.next_node
        return result

    def items(self):
        result = []
        for n in self._list:
            while n:
                result.append((n.key, n.value))
                n = n.next_node
        return result

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.add(key, value)

    def __delitem__(self, key):
        return self.remove(key)

    def __contains__(self, key):
        index = self.get_index(key)
        n = self._list[index]
        while n:
            if n.key is key:
                return True
            n = n.next_node
        return False

    def __iter__(self):
        for n in self._list:
            while n:
                yield n
                n = n.next_node

    def __repr__(self):
        return "{" + ", ".join([repr(x) for x in iter(self)]) + "}"


# Create and Populate with Random Values
print("hm = HashMap(10, 1)\n")
hm = HashMap(10, 1)

print(f"1 in hm: {1 in hm}")
print("hm.add(1, 'a')")
hm.add(1, 'a')
print(f"1 in hm: {1 in hm}\n")

print("hm.add('a', 'a')")
hm.add('a', 'a')
print(f"Capacity: {hm.capacity} \tSize: {hm.size} \thm:{hm!r}\n")

print("Adding: ", end="")
for n in range(8):
    print(f" ({n}:{n})", end="")
    hm.add(n, n)
print(f"\nCapacity: {hm.capacity} \tSize: {hm.size} \thm:{hm}\n")

print("hm.add('A', 'A')")
hm.add('A', 'A')
print(f"Capacity: {hm.capacity} \tSize: {hm.size} \thm:{hm}\n")

print("hm.add('B', 'B')")
hm.add('B', 'B')
print(f"Capacity: {hm.capacity} \tSize: {hm.size} \thm:{hm}\n")

print("hm.keys():", hm.keys())
print("hm.items():", hm.items())
print("hm.values():", hm.values())
print()

print(hm)
