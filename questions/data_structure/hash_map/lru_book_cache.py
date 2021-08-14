"""
    LRU BOOK CACHE (EPI 13.3: IMPLEMENT AN ISBN CACHE)

    Create a book cache for books and prices via their International Standard Book Number (ISBN); the cache should have
    lookup, insert, and remove methods.  Inserting, updating, or looking up an ISBN should update the book as the most
    recently accessed.  Cache eviction should use the Least Recently Used (LRU) policy.

"""
import statistics
import time


# Naive Approach: Use a dictionary/hash map to map ISBNs to time, price tuples.  If an insert were to occur that would
# exceed capacity, then first remove the oldest entry, then insert.
# Time Complexity: See below.
# Space Complexity: O(n), where n is the capacity.
class NaiveLRUBookCache:
    def __init__(self, capacity=10):
        if not isinstance(capacity, int) or capacity <= 0:
            raise TypeError(f"capacity must be an int greater than 0")
        self.capacity = capacity
        self.cache = dict()         # {ISBN: [time, book_price]}

    def __len__(self):
        return len(self.cache)

    def get_oldest_book_isbn(self):
        if self.cache:
            return max(self.cache, key=lambda x: self.cache[x][0])

    def get_oldest_book_name(self):
        if self.cache:
            return max(self.cache, key=lambda x: self.cache[x][2])

    # Time Complexity: O(1).
    def lookup(self, key):
        if key in self.cache:
            self.cache[key][0] = time.time()
            return self.cache[key][1]
        else:
            raise KeyError(f"key: {key!r} not in cache.")

    # Time Complexity: O(1) if cache < capacity, else, O(n), where n is the size of the cache.
    def insert(self, key, price, name):
        if key not in self.cache and len(self.cache) + 1 >= self.capacity:
            oldest_t = None
            oldest_k = None
            for k, (t, _, _) in self.cache.items():
                if oldest_k is None or t < oldest_t:
                    oldest_t = t
                    oldest_k = k
            print(f"\t(delete time:{self.cache[oldest_k][0]}, key:{oldest_k}, price:{self.cache[oldest_k][1]}, "
                  f"name:{self.cache[oldest_k][2]})")
            self.cache.pop(oldest_k)
        self.cache[key] = [time.time(), price, name]

    # Time Complexity: O(1).
    def remove(self, key):
        if key in self.cache:
            return self.cache.pop(key)
        else:
            raise KeyError(f"key: {key!r} not in cache.")

    def __repr__(self):
        return "\n".join([f"\ttime:{v[0]}, key:{k}, price:{v[1]}, name:{v[2]}" for k, v in
                            sorted(self.cache.items(), key=lambda item: item[1][0])])


# Lazy Garbage Collection Approach:  Use a dictionary/hash map to store the books, once the size becomes twice the
# capacity, find and remove all books older than a medium time.  Therefore, the O(n) remove operation occurs at most
# ONCE in every n operations, so the amortized time is O(1).
# Time Complexity: See below.
# Space Complexity: O(2n), which reduces to O(n), where n is the capacity.
#
# NOTE: This approach uses twice as much space as the other approaches.
class LazyGCLRUBookCache:
    def __init__(self, capacity=5):
        if not isinstance(capacity, int) or capacity <= 0:
            raise TypeError(f"capacity must be an int greater than 0")
        self.capacity = capacity
        self.cache = dict()         # {ISBN: [time, book_price]}

    def __len__(self):
        return len(self.cache)

    def get_oldest_book_isbn(self):
        if self.cache:
            return max(self.cache, key=lambda x: self.cache[x][0])

    def get_oldest_book_name(self):
        if self.cache:
            return max(self.cache, key=lambda x: self.cache[x][2])

    # Time Complexity: O(1).
    def lookup(self, key):
        if key in self.cache:
            self.cache[key][0] = time.time()
            return self.cache[key][1]
        else:
            raise KeyError(f"key: {key!r} not in cache.")

    # Time Complexity: O(1) (amortized).  That is, O(1) if cache size < 2 * capacity, if size of cache is 2x capacity,
    # then an O(n) operation will occur, reducing the size of the cache to capacity. Since this only happens at most
    # ONCE every n time, hence, the amortized time complexity will be O(1).
    def insert(self, key, price, name):
        if key not in self.cache and len(self.cache) + 1 >= 2 * self.capacity:
            median_time = statistics.median([value[0] for value in self.cache.values()])
            keys_to_del = [k for k, v in self.cache.items() if v[0] < median_time]
            for k in keys_to_del:
                print(f"\t(delete time:{self.cache[k][0]}, key:{k}, price:{self.cache[k][1]}, "
                      f"name:{self.cache[k][2]})")
                self.cache.pop(k)
        self.cache[key] = [time.time(), price, name]

    # Time Complexity: O(1).
    def remove(self, key):
        if key in self.cache:
            return self.cache.pop(key)
        else:
            raise KeyError(f"key: {key!r} not in cache.")

    def __repr__(self):
        return "\n".join([f"\ttime:{v[0]}, key:{k}, price:{v[1]}, name:{v[2]}" for k, v in
                            sorted(self.cache.items(), key=lambda item: item[1][0])])


# Optimal Dictionary/Hash Map With Linked List Queue Approach:  This approach uses a dictionary/hash map that maps to a
# linked list which maintains the Least Recently Used (LRU) ordering.  When an element is accessed, it moves to the head
# of the linked list.  If when an element is added the number of elements in the cache is greater than the capacity, the
# tail element is removed.
# Time Complexity: See below.
# Space Complexity: O(n), where n is the capacity.


# Linked List Node
class ListNode:
    def __init__(self, key, price=None, name=None, next=None, prev=None):
        self.key = key
        self.price = price
        self.name = name
        self.next = next
        self.prev = prev

    def __iter__(self):
        yield self
        if self.next:
            yield from self.next

    def __repr__(self):
        return f"\t[key:{self.key}, price:{self.price}, name:{self.name}, " \
               f"next:{self.next.key if self.next else None!r}, prev:{self.prev.key if self.prev else None!r}]"


# Class that contains the Linked List (LRU Queue) and Dictionary/Hash Map.
class LRUBookCache:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.mapping = {}  # isbn_str: ListNode
        self.tail = None
        self.head = None

    def __repr__(self):
        if self.head:
            return '\n'.join(map(repr, self.head))
        return f"\tNone"

    def __len__(self):
        return len(self.mapping)

    # Time Complexity: O(1).
    def get_oldest_book_isbn(self):
        if self.tail:
            return self.tail.key

    # Time Complexity: O(1).
    def get_oldest_book_name(self):
        if self.tail:
            return self.tail.name

    # Time Complexity: O(1).
    def move_to_front(self, key):
        if key in self.mapping and self.head is not self.mapping[key]:
            node = self.mapping[key]
            node.prev.next = node.next
            if self.tail is node:
                self.tail = node.prev
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            raise KeyError(f"key: {key!r} not in cache.")

    # Time Complexity: O(1).
    def lookup(self, key):
        if key in self.mapping:
            self.move_to_front(key)
            return self.mapping[key].price
        else:
            raise KeyError(f"key: {key!r} not in cache.")

    # Time Complexity: O(1).
    def remove(self, key):
        if key in self.mapping:
            node = self.mapping[key]
            if self.tail is node:
                self.tail = self.tail.prev if self.tail.prev else None
            if self.head is node:
                self.head = self.head.next
            else:
                node.prev.next = node.next
            return self.mapping.pop(key)

    # Time Complexity: O(1).
    def insert(self, key, price, name):
        if key in self.mapping:
            self.move_to_front(key)
            self.mapping[key].price = price
            self.mapping[key].name = name
        else:
            new_node = ListNode(key, price, name, next=self.head)
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            self.mapping[key] = new_node
            if self.tail is None:
                self.tail = new_node
            if len(self.mapping) >= self.capacity:
                print(f"\t(delete {self.tail})")
                del(self.mapping[self.tail.key])
                self.tail = self.tail.prev
                self.tail.next = None


books = [("978-1408894620", 17.69, "Harry Potter and the Philosopher's Stone [Paperback]"),
         ("978-1408855669", 16.37, "Harry Potter and the Chamber of Secrets, Book 2 Paperback"),
         ("978-1408855911", 18.99, "Harry Potter and the Prisoner of Azkaban: 3/7 (Harry Potter 3) Hardcover"),
         ("978-1408894651", 18.68, "Harry Potter and the Goblet of Fire [Paperback]"),
         ("978-1408855690", 16.71, "Harry Potter and the Order of the Phoenix"),
         ("978-0439784542", 11.98, "Harry Potter and the Half-Blood Prince (Book 6)"),
         ("978-0545010221", 11.98, "Harry Potter and the Deathly Hallows (Book 7)"),
         ("978-1479274833", 34.78, "Elements of Programming Interviews: The Insiders' Guide 2nd Edition"),
         ("978-0984782857", 26.99, "Cracking the Coding Interview: 189 Programming Questions and Solutions 6th Edition"),
         ("978-0451524935", 6.86, "1984 (Signet Classics) Mass Market Paperback"),
         ("978-0345538376", 19.74, "J.R.R. Tolkien 4-Book Boxed Set: The Hobbit and The Lord of the Rings Paperback"),
         ("978-1451673319", 6.94, "Fahrenheit 451 Paperback")]
classes = [NaiveLRUBookCache,
           LazyGCLRUBookCache,
           LRUBookCache]

for cls in classes:
    print(f"\n\n{cls.__name__} Example\n")
    print(f"cache = {cls.__name__}()")
    cache = cls()
    for isbn, price, name in books:
        print(f"print(cache):\n{cache}")
        print(f"cache.insert({isbn}, {price}, {name})")
        cache.insert(isbn, price, name)
    print(f"print(cache):\n{cache}")
    print(f"cache.get_oldest_book_isbn(): {cache.get_oldest_book_isbn()!r} (or, {cache.get_oldest_book_name()!r})")
    print(f"cache.lookup(cache.get_oldest_book_isbn()): {cache.lookup(cache.get_oldest_book_isbn())}")
    print(f"print(cache):\n{cache}")
    for i in range(len(books)-1, len(books) - 4, -1):
        print(f"cache.remove({books[i][0]}): {cache.remove(books[i][0])}")
    print(f"print(cache):\n{cache}")


