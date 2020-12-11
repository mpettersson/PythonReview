r"""
    CLONE LINKED LIST WITH RANDOM LINKS (50CIQ 39: RANDOM LINKED LIST)

    Write a function that accepts the head of a linked list and returns the head of a cloned copy of the provided linked
    list.  In addition to values, the linked list should have links to the next node as well as a random node in the
    list.

    Consider the following linked list:

         ↙‾‾‾\ ↙‾‾‾‾‾‾‾‾‾\
        1 --→ 2 --→ 3 --→ 4
         \_________↗ ↺

    Example:
                head = Node(1, Node(2, Node(3, Node(4))))
                head.rand = head.nxt.nxt
                head.nxt.rand = head
                head.nxt.nxt.rand = head.nxt.nxt
                head.nxt.nxt.nxt.rand = head.nxt
        Input = head  # Or, the linked list above.
        Output = 1  # That is, a new head with value 1 and the same structure as the linked list above.
"""


# Mapping/Dictionary Approach: Use a dictionary to store the mapping of old nodes to new nodes since random links are
# not uniform/the same for all nodes (can go back/forwards any number, including 0).
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(n) BUT uses O(n) for dict.
def clone_linked_list_with_rand_link_dict(ll):
    if ll:
        mapping = {}
        copy = Node(ll.value)
        result = copy
        node = ll
        mapping[node] = copy
        while node.nxt:
            copy.nxt = Node(node.nxt.value)
            node = node.nxt
            copy = copy.nxt
            mapping[node] = copy
        node = ll
        copy = result
        while node:
            copy.rand = mapping[node.rand]
            node = node.nxt
            copy = copy.nxt
        return result


# Copy list without using extra space. Interleave the nodes from the new with the nodes from the original list. Then
# separate the new list from the old.
# Time Complexity:
# Space Complexity: O(n)
def clone_linked_list_with_rand_link(ll):
    if ll:
        node = ll
        while node:
            temp = Node(node.value, node.nxt)
            node.nxt = temp
            node = node.nxt.nxt
        node = ll
        while node:
            node.nxt.rand = node.rand.nxt
            node = node.nxt.nxt
        result = ll.nxt
        node = ll
        while node.nxt:
            tmp = node.nxt
            node.nxt = node.nxt.nxt
            node = tmp
        return result


class Node:
    def __init__(self, value, nxt=None, rand=None):
        self.value = value
        self.nxt = nxt
        self.rand = rand

    def __repr__(self):
        node = self
        result = ["\n\t", "\t", "\t"]
        while node:
            length = max(len(str(node.value)), len(str(node.rand.value if node.rand else None)))
            result[0] += f"{node.value:{length}} → "
            result[1] += f"{'↓':{length}}   "
            result[2] += f"{node.rand.value if node.rand else None:{length}}   "
            node = node.nxt
        result[0] += str(None)
        return "\n".join(result)


linked_list = Node(1, Node(2, Node(3, Node(4))))
linked_list.rand = linked_list.nxt.nxt
linked_list.nxt.rand = linked_list
linked_list.nxt.nxt.rand = linked_list.nxt.nxt
linked_list.nxt.nxt.nxt.rand = linked_list.nxt
fns = [clone_linked_list_with_rand_link_dict,
       clone_linked_list_with_rand_link]

print(f"linked_list: {linked_list}\n")
for fn in fns:
    print(f"{fn.__name__}(linked_list): {fn(linked_list)}\n")


