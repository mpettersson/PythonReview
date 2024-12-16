class HashNode:
    def __init__(self, key, value=None, next_node=None):
        self.key = key
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return f"{self.key}: {self.value}"


class HashMap:
    def __init__(self, init_capacity=10, load_capacity=.7):
        self.size = 0
        print(init_capacity, load_capacity)
        if init_capacity < 1 or load_capacity <= 0 or load_capacity > 1:
            raise ValueError
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
                break
            prev = node
            node = node.next_node

        if not node:
            raise KeyError(key)

        self.size -= 1

        if prev:
            prev.next_node = node.next_node
        else:
            self._list[index] = node.next_node

        return node.value

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
                return
            node = node.next_node

        self.size += 1
        node = self._list[index]
        new_node = HashNode(key, value)
        new_node.next_node = node
        self._list[index] = new_node

        if self.size / self.capacity >= self.load_capacity:
            temp = self._list
            self.capacity = self.capacity * 2
            self.size = 0
            self._list = [None] * self.capacity
            for i in temp:
                while i:
                    self.add(i.key, i.value)
                    i = i.next_node

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

    def __iter__(self):
        for n in self._list:
            while n:
                yield n
                n = n.next_node

    def __repr__(self):
        return "{" + ", ".join([repr(x) for x in iter(self)]) + "}"


import random

# Create and Populate with Random Values
hm = HashMap()
for _ in range(10):
    n = random.randint(0, 1000)
    hm.add(n, n)

print(hm)

# Test Methods
print("len(hm):", len(hm))
print("hm.capacity:", hm.capacity)
print("hm.keys():", hm.keys())
print("hm.items():", hm.items())
print("hm.values():", hm.values())
print()

# Visually Show List
for i, n in enumerate(hm._list):
    print(f"List[{i}]:", n)
    while n:
        print(" key:", n.key, "value:", n.value)
        n = n.next_node

print(hm)
