"""
    LEAST RECENTLY USED (LRU) CACHE

    The Least Recently Used (LRU) Cache is a caching strategy that removes the least recently accessed items first when
    it reaches its storage limit. It follows the Least Recently Used policy to ensure that frequently accessed items
    stay in memory while older, unused items are evicted.

    Several language specific implementations include: Java's LinkedHashMap with access-order mode and Python's
    collections.OrderedDict or functools.lru_cache.

"""

# TODO:
#   - Decide on one or two implementations.
#   - Add documentation/comments.
#   - Add asymptotic times and spaces.


class LRU_Cache:

    def __init__(self, original_function, maxsize=1024):
        self.root = [None, None, None, None]                # Link structure: [PREV, NEXT, KEY, VALUE]
        self.root[0] = self.root[1] = self.root
        self.original_function = original_function
        self.maxsize = maxsize
        self.mapping = {}

    def __call__(self, *key):
        mapping = self.mapping
        root = self.root
        link = mapping.get(key)
        if link is not None:
            link_prev, link_next, link_key, value = link
            link_prev[1] = link_next
            link_next[0] = link_prev
            last = root[0]
            last[1] = root[0] = link
            link[0] = last
            link[1] = root
            return value
        value = self.original_function(*key)
        if len(mapping) >= self.maxsize:
            oldest = root[1]
            next_oldest = oldest[1]
            root[1] = next_oldest
            next_oldest[0] = root
            del mapping[oldest[2]]
        last = root[0]
        last[1] = root[0] = mapping[key] = [last, root, key, value]
        return value

    def keys(self):
        return [v[2][0] for v in self.mapping.values()]

    def values(self):
        return [v[3] for v in self.mapping.values()]

    def items(self):
        return [(v[2][0], v[3]) for v in self.mapping.values()]


# p = LRU_Cache(ord, maxsize=3)
# for c in 'abcdecaeaa':
#     print(c, p(c))
# print("p.keys()", p.keys())
# print("p.values()", p.values())
# print("p.items()", p.items())




from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int = 10):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        raise KeyError(f"{key} not in cache.")

    def put(self, key, value=None) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def __repr__(self):
        return f"{self.cache}"

# cache = LRUCache(14)
#
# for i in range(25):
#     print(f"cache.put({i}): {cache.put(i)}")
#     print("cache:", cache)
#
# exit()
#
# cache.put(1, 1)
# print(cache.cache)
# cache.put(2, 2)
# print(cache.cache)
# cache.get(1)
# print(cache.cache)
# cache.put(3, 3)
# print(cache.cache)
# print("cache:", cache)
# try:
#     cache.get(2)
# except KeyError as ke:
#     print(ke)
# print(cache.cache)
# cache.put(4, 4)
# print(cache.cache)
# try:
#     cache.get(1)
# except KeyError as ke:
#     print(ke)
# print(cache.cache)
# cache.get(3)
# print(cache.cache)
# cache.get(4)
# print(cache.cache)


# SEE: https://leetcode.com/problems/lru-cache/solution/
from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return - 1
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

    def __repr__(self):
        return repr(self.items())
# Your LRUCache object will be instantiated and called as such:

obj = LRUCache(2)
param_1 = obj.get(3)
obj.put(5, "five")
obj.put(6, "six")
obj.put(7, "seven")
print('adsf', obj)


class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache():
    def _add_node(self, node):
        # Always add the new node right after head.
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)  # NOTE
        return node.value

    def put(self, key, value):
        node = self.cache.get(key)
        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value
            self.cache[key] = newNode
            self._add_node(newNode)
            self.size += 1
            if self.size > self.capacity:  # NOTE
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)


