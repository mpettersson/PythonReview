class HashNode:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class HashMap:
    def __init__(self, initial_size=10):
        self.list = [None] * initial_size
        self.capacity = initial_size
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return True if self.size == 0 else False

    def keys(self):
        key_list = []
        for node in self.list:
            while node is not None:
                key_list.append(node.key)
                node = node.next
        return key_list

    # Get Index
    def get_index(self, key):
        return hash(key) % self.capacity

    # Remove
    def remove(self, key):
        index = self.get_index(key)
        head = self.list[index]
        prev = None

        while head:
            if head.key is key:
                break
            prev = head
            head = head.next

        if not head:
            return None

        self.size -= 1

        if prev:
            prev.next = head.next
        else:
            self.list[index] = head.next

        return head.value

    # Get
    def get(self, key):
        head = self.list[self.get_index(key)]
        while head:
            if head.key is key:
                return head.value
            head = head.next
        return None

    # Add
    def add(self, key, value):
        index = self.get_index(key)
        head = self.list[index]

        while head:
            if head.key is key:
                head.value = value
                return
            head = head.next

        self.size += 1
        head = self.list[index]
        new_node = HashNode(key, value)
        new_node.next = head
        self.list[index] = new_node

        # If load factor goes beyond threshold then double size of the list
        if self.size / self.capacity >= .7:
            temp = self.list
            self.capacity = self.capacity * 2
            self.size = 0
            self.list = [None] * self.capacity
            for i in temp:
                while i is not None:
                    self.add(i.key, i.value)
                    i = i.next

import random

ht = HashMap()
for _ in range(10):
    i = random.randint(0, 1000)
    ht.add(i, i)
print("ht.size():", ht.get_size())
print("ht.capacity: ", ht.capacity)

for i in range(len(ht.list)):
    head = ht.list[i]
    if head is not None:
        print(i, "values:")
        while head is not None:
            print(" key:", head.key, "value:", head.value)
            head = head.next

