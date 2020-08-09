"""
    LINKED LIST

    A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations,
    rather, each node has (at least) one pointer to the next node in the data structure. Single linked lists have only
    one pointer, where doubly linked list have a second pointer pointing to the previous node.
"""


class _DNode:
    def __init__(self, value=None, prev=None, next=None):
        """Initialize self.  See help(type(self)) for accurate signature."""
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        """Return repr(self)."""
        return repr(self.value)


class _SNode:
    def __init__(self, value, next=None):
        """Initialize self.  See help(type(self)) for accurate signature."""
        self.value = value
        self.next = next

    def __str__(self):
        """Return str(self)."""
        return str(self.value)

    def __repr__(self):
        """Return repr(self)."""
        return repr(self.value)


class SLinkedList:
    def __init__(self, *args):
        """Initialize self.  See help(type(self)) for accurate signature."""
        self._head = None
        self._len = 0
        if len(args) > 0:
            for i in reversed(args):
                self._head = _SNode(i, self._head)
                self._len += 1

    def __iter__(self):
        """Implement iter(self)."""
        node = self._head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        """Return repr(self)."""
        return f"[{', '.join(map(repr, self))}]"

    def __len__(self):
        """Return len(self)."""
        return self._len

    def __getitem__(self, index):
        """x.__getitem__(y) <==> x[y]"""
        if 0 <= abs(index) < self._len:
            if index < 0:
                index = self._len + index
            node = self._head
            i = 0
            while i < index:
                node = node.next
                i += 1
            return node
        raise IndexError("SLinkedList index out of range")

    def __setitem__(self, index, value):
        """x.__setitem__(index, value) <==> x[index] = value"""
        if 0 <= abs(index) < self._len:
            if index < 0:
                index = self._len + index
            node = self._head
            i = 0
            while i < index:
                node = node.next
                i += 1
            node.value = value
            return
        raise IndexError("SLinkedList index out of range")

    def insert(self, index, object):
        """Insert object before index."""
        if index < 0:
            index = self._len + index
        if not self._head or index <= 0:
            self._head = _SNode(object, self._head)
        else:
            prev = None
            node = self._head
            i = 0
            while node and i < index:
                prev = node
                node = node.next
                i += 1
            prev.next = _SNode(object, node)
        self._len += 1

    def pop(self, index=-1):
        """Remove and return item at index (default last).
        Raises IndexError if list is empty or index is out of range."""
        if index < 0:
            index = self._len + index
        if 0 <= index < self._len:
            node = self._head
            prev = None
            i = 0
            while i < index:
                prev = node
                node = node.next
                i += 1
            item = node.value
            if prev:
                prev.next = node.next
            else:
                self._head = node.next
            self._len -= 1
            return item
        raise IndexError("SLinkedList index out of range")

    def reverse(self):
        """Reverse node order in list."""
        node = self._head
        h = None
        while node:
            nxt = node.next
            node.next = h
            h = node
            node = nxt
        self._head = h

    def reverse_rec(self):
        def wrapper(head, length):
            if not head or length < 1:
                return head
            if length is 1:
                return head.next
            if length is 2:
                head.value, head.next.value = head.next.value, head.value
                return head.next.next
            node = wrapper(head.next, length - 2)
            head.value, node.value = node.value, head.value
            return node.next
        wrapper(self._head, self._len)

    def sort(self):
        pass

    def remove(self, value):
        """Remove first occurrence of value.\nRaises ValueError if the value is not present."""
        node = self._head
        prev = None
        while node:
            if node.value == value:
                if prev:
                    prev.next = node.next
                else:
                    self._head = node.next
                self._len -= 1
                return
            prev = node
            node = node.next
        raise ValueError("SLinkedList.remove(x): x not in linked list")

    def clear(self):
        """Remove all items from list."""
        self._head = None
        self._len = 0

    def append(self, object):
        """Append object to the end of the list."""
        self.insert(len(self), object)

    def index(self, value):
        """Return first index of value.\nRaises ValueError if the value is not present."""
        node = self._head
        i = 0
        while node:
            if node.value is value:
                return i
            node = node.next
            i += 1
        raise ValueError(f"'{value}' is not in SLinkedList")


print("\nINIT")
sll = SLinkedList()
print(f"sll: {sll}")
del sll
sll = SLinkedList(0)
print(f"sll: {sll}")
del sll
sll = SLinkedList(0, 0, "A", 0, 0, None, 1, "2", None, "z", None)
print(f"sll: {sll}")
del sll
sll = SLinkedList("A")
print(f"sll: {sll}")

print("\nSTR & REPR")
print(f"str(sll): {str(sll)}")
print(f"repr(sll): {repr(sll)}")

print("\nINSERT")
print(f"l: {sll}")
print(f"sll.insert(4, 4): {sll.insert(4, 4)}")
print(f"l: {sll}")
print(f"sll.insert(1, 7): {sll.insert(1, 7)}")
print(f"l: {sll}")
print(f"sll.insert(-1, 'last'): {sll.insert(-1, 'last')}")
print(f"l: {sll}")
print(f"sll.insert(0, 'Z'): {sll.insert(0, 'Z')}")
print(f"l: {sll}")
print(f"sll.insert(-100, 'zZ'): {sll.insert(-100, 'zZ')}")

print("\nAPPEND")
print(f"l: {sll}")
print(f"sll.append(7): {sll.append(7)}")
print(f"l: {sll}")
print(f"sll.append(None): {sll.append(None)}")
print(f"l: {sll}")

print("\nINDEX")
print(f"l.index('zZ'): {sll.index('zZ')}")
print(f"l.index(7): {sll.index(7)}")
print(f"l.index(None): {sll.index(None)}")
try:
    print(f"sll.index(96): {sll.index(96)}")
except ValueError as e:
    print("ValueError:", e.args)

print("\nGETITEM")
print(f"l: {sll}")
print(f"sll[0]: {sll[0]}")
print(f"sll[1]: {sll[1]}")
print(f"sll[len(sll1) - 1]: {sll[len(sll) - 1]}")

print("\nSETITEM")
print(f"sll: {sll}")
print("sll[0]='wat'"); sll[0] = 'wat'
print("sll[1]=420"); sll[1] = 420
print("sll[len(l) - 3]=None"); sll[len(sll) - 3] = None
print(f"sll: {sll}")

print("\nPOP")
sll.append('42')
sll.append(77)
print(f"sll: {sll}")
print(f"sll.pop(): {sll.pop():}")
print(f"sll: {sll}")
print(f"sll.pop(len(sll)-1): {sll.pop(len(sll)-1):}")
print(f"sll: {sll}")
print(f"sll.pop(-3): {sll.pop(-3):}")
print(f"sll: {sll}")
print(f"sll.pop(0): {sll.pop(0):}")
print(f"sll: {sll}")

print("\nITER")
for n in sll:
    print(f"n: {n}")

print("\nCLEAR")
print(f"sll.clear(): {sll.clear()}")
print(f"l: {sll}")

print("\nREVERSE")
sll = SLinkedList(0, 0, "A", 0, 0, None, 1, "2", None, "z", None)
print(f"sll: {sll}")
print(f"sll.reverse(): {sll.reverse()}")
print(f"sll: {sll}")
sll = SLinkedList(*list(range(10000)))
print(f"sll[9999]: {sll[9999]}")
print(f"sll.reverse(): {sll.reverse()}")
print(f"sll[9999]: {sll[9999]}")




