r"""
    MERGE TWO SORTED LINKED LISTS (leetcode.com/problems/merge-two-sorted-lists)

    Write a function, that accepts two sorted (in non-descending order) linked lists, then merges and returns a single
    sorted (in non-descending order) linked list.

    Consider the following linked lists:
        1 ⟶ 3 ⟶ 5 ⟶ 7
        2 ⟶ 4 ⟶ 6
    The result of merging the above (3) linked lists:
        1 ⟶ 2 ⟶ 3 ⟶ 4 ⟶ 5 ⟶ 6 ⟶ 7

    Example:
                l_1 = Node(1, Node(3, Node(5, Node(7)))),   # Or, the 1st linked list (above).
                l_2 = Node(2, Node(4, Node(6)))             # Or, the 2nd linked list (above).
        Input = l_1, l_2
        Output = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))  # Or, the 3rd list (above).
"""
import copy


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Should I modify the given lists?
#   - What are the possible number of lists?


# APPROACH: Naive Via Sort
#
# Construct a (python) list consisting of the values from each of the two linked lists, then sort the (python) list,
# finally, create and return a linked list from the sorted (python) list.
#
# Time Complexity: O(m + n), where m and n are the number of elements in l1 and l2.
# Space Complexity: O(m + n), where m and n are the number of elements in l1 and l2.
def merge_two_sorted_linked_lists_naive(l1, l2):
    if l1 and not l2:
        return l1
    if l2 and not l1:
        return l2
    if l1 and l2:
        l = [e for e in l1] + [e for e in l2]  # Can do this because Node has __iter__ method.
        l.sort()
        result = tail = Node(l.pop(0))
        while l:
            tail.next = Node(l.pop(0))
            tail = tail.next
        return result


# APPROACH: Via Recursion
#
# This approach recursively checks if l1 or l2 is empty, if so, then the other list is returned.  If both lists exist,
# then the list with the smaller first value is returned, after it's next node is updated as the (recursive) result of
# the function (called on it's next node with the other list).
#
# Time Complexity: O(m + n), where m and n are the number of elements in l1 and l2.
# Space Complexity: O(m + n), where m and n are the number of elements in l1 and l2.
def merge_two_sorted_linked_lists_rec(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.value < l2.value:
        l1.next = merge_two_sorted_linked_lists_rec(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_sorted_linked_lists_rec(l1, l2.next)
        return l2


# APPROACH: (Optimal) Iterative
#
# This approach simply uses a temporary node object to build a merged list from the two lists.  The two lists (heads)
# are compared, the one with the minimal value is added to the tail of the temp node, and is updated as the next node.
# This continues until at least one of the lists has become None.  Then, the tail of the temporary list is directed to
# point at the other list (which may also be None).  Once done, temp.next is returned as the result.
#
# Time Complexity: O(m + n), where m and n are the number of elements in l1 and l2.
# Space Complexity: O(1).
def merge_two_sorted_linked_lists(l1, l2):
    temp = prev = Node(-float("inf"))   # temp.next = result
    # NOTE: The temp (Node) has a value less than any values in l1 or l2, and is used as the 'result' variable; where
    #       temp.next is the actual return value (NOT temp).  This is done to MINIMIZE the code.
    while l1 and l2:
        if l1.value <= l2.value:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
    prev.next = l1 if l1 else l2        # In case either of the lists still have values.
    return temp.next                    # REMEMBER, temp.next is the result (temp is just a pointer).


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __iter__(self):
        yield self.value
        if self.next:
            yield from self.next

    def __repr__(self):
        return ' ⟶ '.join(map(repr, self))


args_list = [(Node(1, Node(3, Node(5, Node(7)))),
              Node(2, Node(4, Node(6)))),
             (Node(1, Node(3, Node(5, Node(7, Node(9))))),
              Node(0, Node(2, Node(4, Node(6, Node(8)))))),
             (Node(0, Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))),
              Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10))))))))))),
             (Node(-8, Node(-2, Node(-4, Node(6, Node(8))))),
              Node(-9, Node(-7, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9))))))))))),
             (Node(1, Node(3, Node(5, Node(7)))),
              None),
             (None, None)]
fns = [merge_two_sorted_linked_lists_naive,
       merge_two_sorted_linked_lists_rec,
       merge_two_sorted_linked_lists]

for l1, l2 in args_list:
    print(f"l1: {l1}\nl2: {l2}")
    for fn in fns:
        print(f"{fn.__name__}(args): {fn(copy.deepcopy(l1), copy.deepcopy(l2))}")
    print()


