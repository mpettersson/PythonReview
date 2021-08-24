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


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Clarify the question (previous link, what can random point to, what can't random point to, can nodes be marked,
#     duplicate values, is a repeated, what are the values data type)?


# APPROACH: Mapping/Dictionary
#
# Observations:
#   - Create all nodes first to prevent a link from referencing a non-existing node (if attempted in one pass).
#   - There needs to be a way to correlate random links from the original list to the cloned list; the relation, or
#     order, must exist, or be maintained.
#
# This approach uses a dictionary to be able to maintain the correlation, or the mapping, from a node to its linked
# random node.  T
# nodes (can go back/forwards any number, including 0).
#
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(n), where n is the number of nodes in the linked list.
#
# NOTE: These two approaches have a time/space tradeoff; this approach uses one less iteration over the nodes, but uses
#       an additional data structure (dict) to store a reference to all of the nodes.  Discuss this difference with the
#       interviewer, asking if they have a preference.
def clone_linked_list_with_rand_link_dict(head):
    if head:
        mapping = {}
        copy = Node(head.value)
        result = copy
        node = head
        mapping[node] = copy
        while node.nxt:                         # First iteration; clone a new list using only the next pointers.
            copy.nxt = Node(node.nxt.value)
            node = node.nxt
            copy = copy.nxt
            mapping[node] = copy                    # However, add the relation of node to cloned node in a dictionary.
        node = head
        copy = result
        while node:                             # Second iteration across the nodes:
            copy.rand = mapping[node.rand]          # This time, use the dictionary to assign the random links.
            node = node.nxt
            copy = copy.nxt
        return result


# APPROACH: Interleave Then Separate Cloned Nodes
#
# This approach duplicates the cloned nodes in the original list, thus lowering additional overhead (O(n) dict): simply
# iterate over the nodes, interleaving new/cloned nodes after each original node in the list. This allows for the second
# iteration to be able to correctly reference the random nodes.  Then, one last iteration over the nodes separates the
# new/cloned nodes from the original nodes to a new list.  Return the head of the new/cloned list.
#
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(n) (DOESN'T uses a dict), where n is the number of nodes in the linked list.
#
# NOTE: These two approaches have a time/space tradeoff; this approach uses one additional iteration over the nodes,
#       however, it does NOT use an additional data structure (dict) to store the nodes.  Discuss this difference with
#       the interviewer, asking if they have a preference.
def clone_linked_list_with_rand_link(head):
    if head:
        node = head
        while node:                             # 1st Iteration: Create new/cloned nodes after each node in the original
            temp = Node(node.value, node.nxt)   # list w/o links to their respective random nodes.
            node.nxt = temp
            node = node.nxt.nxt
        node = head
        while node:                             # 2nd Iteration: Traverse the list adding the respective random links.
            node.nxt.rand = node.rand.nxt
            node = node.nxt.nxt
        result = head.nxt
        node = head
        while node.nxt:                         # 3rd Iteration: Separate the cloned and original lists.
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


linked_list = Node(1, Node(2, Node(3, Node(4))))    # Linked list (See Example Above): 1 -> 2 -> 3 -> 4 -> None
linked_list.rand = linked_list.nxt.nxt              # 1.rand -> 3
linked_list.nxt.rand = linked_list                  # 2.rand -> 1
linked_list.nxt.nxt.rand = linked_list.nxt.nxt      # 3.rand -> 3
linked_list.nxt.nxt.nxt.rand = linked_list.nxt      # 4.rand -> 2
fns = [clone_linked_list_with_rand_link_dict,
       clone_linked_list_with_rand_link]

print(f"linked_list: {linked_list}\n")
for fn in fns:
    print(f"{fn.__name__}(linked_list): {fn(linked_list)}\n")


