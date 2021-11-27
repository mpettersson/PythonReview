"""
    LRU (LEAST RECENTLY USED) CACHE

    Design and build a "least recently used" cache, which evicts the least recently used item.  The cache should map
    from keys to values (allowing you to insert and retrieve a value associated with a particular key) and be
    initialized with a max size.  When it is full, it should evict the least recently used item.  You can assume the
    keys are integers and the values are strings.

    Note, scoping gives us the following requirements:
        - Inserting Key, Value Pair:  Need to be able to insert (key, value) pair
        - Retrieving Values by Key:  Need to be able to retrieve the value via key.
        - Finding Least Recently Used:  Know the least used item (and likely, the usage ordering of all items)
        - Updating Most Recently Used:  When retrieving a value via key, update the order to be the most used item.
        - Eviction:  Should have max capacity and should remove least recently used item when it hits capacity.

    Using a HashTable/Dictionary to point to a Linked List sounds like the way to go...

    Using the scoped requirements, we can easily outline the needed algorithms:
        Inserting Key, Value Pair:  Create a linked list node with key, value.  Insert into head of linked list.
                                    Insert key -> node mapping into dictionary.
        Retrieving Value by Key:  Look up node in hash table and return value.  Update most recently used item.
        Finding Least Recently Used:  Least recently used item will be found at the end of the linked list.
        Updating Most Recently Used:  Move node to front of linked list.  (Dictionary doesn't need to be updated)
        Eviction:  Remove tail of linked list.  Get key from linked list and remove key from dictionary.
"""
from collections import OrderedDict


# TODO: ADD SOLUTIONS FROM https://leetcode.com/problems/lru-cache/solution/
class LRUCache(OrderedDict):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        super().__init__()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCacheViaLinkedList:
    def __init__(self, max_size):
        self._max_size = max_size
        self._map = {}
        self._list_head = None
        self._list_tail = None

    # Get value for key and mark as most recently used.
    def get_value(self, key):
        item = self._map[key]
        if item is None:
            return None
        # Move to front of list to mark as most recently used.
        if item != self._list_head:
            self._remove_from_linked_list(item)
            self._insert_at_front_of_linked_list(item)
        return item.value

    # Remove node from linked list.
    def _remove_from_linked_list(self, node):
        if node is None:
            return
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node == self._list_tail:
            self._list_tail = node.prev
        if node == self._list_head:
            self._list_head = node.next

    # Insert node at front of linked list.
    def _insert_at_front_of_linked_list(self, node):
        if self._list_head is None:
            self._list_head = node
            self._list_tail = node
        else:
            self._list_head.prev = node
            node.next = self._list_head
            self._list_head = node

    # Remove key/value pair from cache, deleting from dict and linked list
    def remove_key(self, key):
        node = self._map[key]
        self._remove_from_linked_list(node)
        del self._map[key]
        return True

    # Put key/value pair in cache.  Removes old value for key if necessary.  Inserts pair into linked list and dict.
    def set_key_value(self, key, value):
        # Remove if already there.
        if key in self._map.keys():
            self.remove_key(key)
        # If full, remove least recently used item from cache.
        if len(self._map) >= self._max_size and self._list_tail is not None:
            self.remove_key(self._list_tail.value)
        # Insert new node.
        node = LinkedListNode(key, value)
        self._insert_at_front_of_linked_list(node)
        self._map[key] = node

    def __str__(self):
        node = self._list_head
        result = "Max Size:%d {" % self._max_size
        while node is not None:
            result += "%d:%s" % (node.value, node.value)
            if node is self._list_tail:
                break
            node = node.next
            result += ", "
        result += "}"
        return str(result)


least_recently_used_cache = LRUCacheViaLinkedList(4)
print("least_recently_used_cache:", least_recently_used_cache, "\n")
print("least_recently_used_cache.set_key_value(0, \"Zero\")"); least_recently_used_cache.set_key_value(0, "Zero")
print("least_recently_used_cache.set_key_value(1, \"One\")"); least_recently_used_cache.set_key_value(1, "One")
print("least_recently_used_cache.set_key_value(2, \"Two\")"); least_recently_used_cache.set_key_value(2, "Two")
print("\nleast_recently_used_cache:", least_recently_used_cache, "\n")
print("least_recently_used_cache.set_key_value(3, \"Three\")"); least_recently_used_cache.set_key_value(3, "Three")
print("least_recently_used_cache.set_key_value(4, \"Four\")"); least_recently_used_cache.set_key_value(4, "Four")
print("least_recently_used_cache.set_key_value(5, \"Five\")"); least_recently_used_cache.set_key_value(5, "Five")
print("\nleast_recently_used_cache:", least_recently_used_cache)











