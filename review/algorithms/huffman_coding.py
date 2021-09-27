"""
    HUFFMAN CODING

    Encode:
        Average Runtime:    O(n log(n)), where n is the number of symbols.
        Worst Runtime:      O(n log(n)), where n is the number of symbols.
        Best Runtime:       O(n), where n is the number of symbols, if the symbols are sorted by probability.
    Decode:
        Runtime:    O(log(n)), where n is the number of symbols.
    Space Complexity:   O(n), where n is the size of the alphabet of symbols.

    In 1951 at MIT, David A. Huffman wrote a term paper on the problem of finding the most efficient binary code via a
    frequency-sorted binary tree.

    Huffman coding, when given a set of symbols and their weights (usually proportional to probabilities), produces a
    prefix-free binary code with minimum expected codeword length.  Where a prefix-free code, or prefix code, is a bit
    string representing a symbol that is never a prefix of the bit string representing any other symbol.

    Algorithm:
        The simplest construction algorithm uses a priority queue where the node with lowest probability is given
        highest priority:

            1. Create a leaf node for each symbol and add it to the priority queue.
            2. While there is more than one node in the queue:
                (a) Remove the two nodes of highest priority (lowest probability) from the queue
                (b) Create a new internal node with these two nodes as children and with probability equal to the sum of
                    the two nodes' probabilities.
                (c) Add the new node to the queue.
            3. The remaining node is the root node and the tree is complete.

        Once the Huffman tree has been generated, it is traversed to generate a dictionary which maps the symbols to
        binary codes as follows:

            1. Start with current node set to the root.
            2. If node is not a leaf node, label the edge to the left child as 0 and the edge to the right child as 1.
               Repeat the process at both the left child and the right child.

        The final encoding of any symbol is then read by a concatenation of the labels on the edges along the path from
        the root node to the symbol.

    TODO:
        - Add Example
        - Beautify The Display Function

    References:
        - https://youtu.be/B3y0RsVCyrw
        - http://compression.ru/download/articles/huff/huffman_1952_minimum-redundancy-codes.pdf
"""
import heapq


class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch                                            # Only Populated If LEAF Node!
        self.freq = freq                                        # If LEAF then ch freq ELSE SUM of ALL Descendants freq.
        self.value = self.freq if self.ch is None else self.ch  # TODO: Used for display fn, need to modify display fn.
        self.left = left                                        # Either NO children, or TWO children (never ONE child).
        self.right = right                                      # Either NO children, or TWO children (never ONE child).

    def __lt__(self, other):                                    # REQUIRED for priority queue/min heap.
        return self.freq < other.freq


def get_huffman_tree(text):
    if len(text) > 0:
        freq = {ch: text.count(ch) for ch in set(text)}
        priority_queue = [Node(k, v) for k, v in freq.items()]
        heapq.heapify(priority_queue)
        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)                # Get node with lowest available frequency.
            right = heapq.heappop(priority_queue)               # Get node with lowest available frequency.
            heapq.heappush(priority_queue, Node(None, left.freq + right.freq, left, right))
        return priority_queue[0]                                # Only root left (i.e., len(priority_queue) == 1)!


def display(node):
    def wrapper(node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        if node.right is None and node.left is None:  # No child.
            return [str(node.value)], len(str(node.value)), 1, len(str(node.value)) // 2
        if node.right is None:  # Only left child.
            lines, n, p, x = wrapper(node.left)
            u = len(str(node.value))
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + str(node.value)
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        if node.left is None:  # Only right child.
            lines, n, p, x = wrapper(node.right)
            u = len(str(node.value))
            first_line = str(node.value) + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        else:  # Two children.
            left, n, p, x = wrapper(node.left)
            right, m, q, y = wrapper(node.right)
            u = len(str(node.value))
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + str(node.value) + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zip(left, right)]
            return lines, n + m + u, max(p, q) + 2, n + u // 2
    if node:
        lines, _, _, _ = wrapper(node)
        for line in lines:
            print(line)


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
       "dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex " \
       "ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat " \
       "nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit " \
       "anim id est laborum."
display(get_huffman_tree(text))


