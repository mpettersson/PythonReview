"""
    SUM LISTS (CCI 2.5)

    You have two numbers represented by a linked list, where each node contains a single digit.  The digits are stored
    in reverse order, such that the 1's digit is at the head of the list.  Write a function that adds the two numbers
    and returns the sum as a linked list.

    Example:
        Input:  7 -> 1 -> 6 -> None, 5 -> 9 -> 2 -> None (that is, 617 + 295)
        Output: 2 -> 1 -> 9 -> None (or, the sum 912)

    Variation:
        Suppose the digits are stored in forward order. Repeat the above problem.
"""


# Naive Solution:  Convert lists numbers, add, then convert the result to a list and return.  The time and space
# complexity is O(n) where n is the length of the longest list.
# NOTE: This probably isn't the solution the interviewer is looking for...
def sum_lists_reversed_order_naive(l1, l2):
    if l1 or l2:
        v1 = []
        v2 = []
        while l1:
            v1.insert(0, str(l1.value))
            l1 = l1.next
        while l2:
            v2.insert(0, str(l2.value))
            l2 = l2.next
        v = str(int("".join(v1)) + int("".join(v2)))
        h = t = None
        for c in reversed(v):
            if h:
                t.next = LinkedList(c)
                t = t.next
            else:
                h = t = LinkedList(c)
        return h


# Recursive Solution:  The time and space complexity is O(n) where n is the length of the longest list.
def sum_lists_reversed_order_rec(l1, l2, carry=0):
    if not l1 and not l2 and carry == 0:
        return None
    value = carry
    if l1:
        value += l1.value
    if l2:
        value += l2.value
    res = LinkedList(value % 10)
    if l1 or l2:
        more = sum_lists_reversed_order_rec(l1.next if l1 else None, l2.next if l2 else None, 1 if value >= 10 else 0)
        res.next = more
    return res


# Iterative Solution:  The time and space complexity is O(n) where n is the length of the longest list.
def sum_lists_reversed_order(l1, l2):
    n1 = l1
    n2 = l2
    h = t = None
    carry = 0
    while n1 or n2 or carry:
        v1 = n1.value if n1 else 0
        v2 = n2.value if n2 else 0
        val = (v1 + v2 + carry) % 10
        carry = (v1 + v2 + carry) // 10
        if h:
            t.next = LinkedList(val)
            t = t.next
        else:
            h = t = LinkedList(val)
        if n1:
            n1 = n1.next
        if n2:
            n2 = n2.next
    return h


# (Variation) Naive Solution:  Convert lists numbers, add, then convert the result to a list and return.  The time and
# space complexity is O(n) where n is the length of the longest list.
# NOTE: This probably isn't the solution the interviewer is looking for...
def sum_lists_forward_order_naive(l1, l2):
    if l1 or l2:
        v1 = []
        v2 = []
        while l1:
            v1.append(str(l1.value))
            l1 = l1.next
        while l2:
            v2.append(str(l2.value))
            l2 = l2.next
        v = str(int("".join(v1)) + int("".join(v2)))
        h = t = None
        for c in v:
            if h:
                t.next = LinkedList(int(c))
                t = t.next
            else:
                h = t = LinkedList(int(c))
        return h


# (Variation) Recursive Solution:  The time and space complexity is O(n) where n is the length of the longest list.
def sum_lists_forward_order_rec(l1, l2):
    if l1 and l2:
        len1 = length(l1)
        len2 = length(l2)
        if len1 < len2:
            l1 = pad_list(l1, abs(len1 - len2))
        elif len2 < len1:
            l2 = pad_list(l2, abs(len1 - len2))

        def wrapper(l1, l2):
            if not l1 and not l2:
                return None, 0
            h, carry = wrapper(l1.next, l2.next)
            return (LinkedList((carry + l1.value + l2.value) % 10, h)), ((carry + l1.value + l2.value) // 10)

        h, c = wrapper(l1, l2)
        if c:
            h = LinkedList(c, h)
        return h
    return l1 if l1 else l2


# Helper Function
def length(l):
    if l:
        i = 0
        while l:
            i += 1
            l = l.next
        return i


# Helper Function
def pad_list(l, num=1):
    if l and num >= 1:
        for _ in range(num):
            l = LinkedList(0, l)
    return l


class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value) + " -> " + (repr(self.next) if self.next else "None")


l0 = LinkedList(9, LinkedList(9, LinkedList(9, LinkedList(9))))
l1 = LinkedList(7, LinkedList(1, LinkedList(6)))
l2 = LinkedList(5, LinkedList(9, LinkedList(2)))
l3 = LinkedList(1)
l4 = LinkedList(0)
l5 = None

args = [(l0, l1), (l1, l2), (l1, l3), (l0, l3), (l3, l3), (l4, l4), (l0, l4), (l5, l5)]

for (a1, a2) in args:
    print(f"sum_lists_reversed_order_naive({a1}, {a2}) = {sum_lists_reversed_order_naive(a1, a2)}")
print()

for (a1, a2) in args:
    print(f"sum_lists_reversed_order_rec({a1}, {a2}) = {sum_lists_reversed_order_rec(a1, a2)}")
print()

for (a1, a2) in args:
    print(f"sum_lists_reversed_order({a1}, {a2}) = {sum_lists_reversed_order(a1, a2)}")
print()

for (a1, a2) in args:
    print(f"sum_lists_forward_order_naive({a1}, {a2}) = {sum_lists_forward_order_naive(a1, a2)}")
print()

for (a1, a2) in args:
    print(f"sum_lists_forward_order_rec({a1}, {a2}) = {sum_lists_forward_order_rec(a1, a2)}")


