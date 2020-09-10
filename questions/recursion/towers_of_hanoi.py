"""
    TOWERS OF HANOI (CCI 8.6)

    In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide
    onto any tower.  The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each
    disk sits on top of an even larger one).  You have the following constraints:

        1. Only one disk can be moved at a time.
        2. A disk is slid off the top of one tower onto the next tower.
        3. A disk can only be placed on top of a larger disk.

    Write a program to move the disks from the first tower to the last using stacks.
"""
import time


# Recursive (Using List as Stacks) Approach: Time complexity is O(2**n) and space complexity is O(n).
def toh(n):

    def _toh(n, orig, dest, buff):
        if n is 0:                      # Base Case
            return
        _toh(n - 1, orig, buff, dest)   # Move top n - 1 disks from orig to buffer, using dest as buffer
        dest.insert(0, orig.pop(0))     # Move top from origin to dest
        _toh(n - 1, buff, dest, orig)   # Move top n - 1 disks from buffer to dest, using orig as buffer

    if n is not None and n >= 0:
        a = []
        b = []
        c = []
        for i in range(n, 0, -1):
            a.insert(0, i)
        # print(f"A: {a}\nB: {b}\nC: {c}\n")
        _toh(n, a, c, b)
        # print(f"A: {a}\nB: {b}\nC: {c}\n")


# Recursive (Using Stacks Objects) Approach: Time complexity is O(2**n) and space complexity is O(n).
def towers_of_hanoi(n):

    def _move_disks(n, orig, dest, buff):
        if n is 0:  # Base Case
            return
        _move_disks(n - 1, orig, buff, dest)  # Move top n - 1 disks from orig to buffer, using dest as buffer
        dest.push(orig.pop())  # Move top from origin to dest
        _move_disks(n - 1, buff, dest, orig)  # Move top n - 1 disks from buffer to dest, using orig as buffer

    if n is not None and n >= 0:
        s1 = Stack()
        s2 = Stack()
        s3 = Stack()
        for i in range(n, 0, -1):
            s1.push(i)
        # print(f"A: {s1}\nB: {s2}\nC: {s3}\n")
        _move_disks(n, s1, s3, s2)
        # print(f"A: {s1}\nB: {s2}\nC: {s3}\n")


# Binary Counting Approach: Time complexity is O(2**n) and space complexity is O(1).
# SEE: https://en.wikipedia.org/wiki/Tower_of_Hanoi#Binary_solution For more algorithm information...
def towers_of_hanoi_bin_counting(num):

    def _towers_of_hanoi_bin_counting(stack_list):
        num_moves = 2 ** stack_list[0].size
        i = 0
        while i < num_moves:
            # If the one bit changed, move disk 0 one peg to the right, if at left peg, move to rightmost peg.
            if (i + 1) & 1 is 1:
                for x in range(len(stack_list)):
                    if stack_list[x].peek() == 0:
                        # print("moving disk 0 from peg", x, "to", ((x + 1) % 3))
                        stack_list[((x + 1) % 3)].push(stack_list[x].pop())
                        break
            # If a roll over occurred, i.e.
            else:
                val = (i ^ (i + 1)) >> 1
                disk_num = 0
                while val > 0:
                    disk_num += 1
                    val = val >> 1
                for x in range(len(stack_list)):
                    if stack_list[x].peek() == disk_num:
                        if stack_list[((x + 1) % 3)].empty() or stack_list[((x + 1) % 3)].peek() > disk_num:
                            # print("moving disk", disk_num, "from peg", x, "to", ((x + 1) % 3))
                            stack_list[((x + 1) % 3)].push(stack_list[x].pop())
                        else:
                            # print("moving disk", disk_num, "from peg", x, "to", ((x + 2) % 3))
                            stack_list[((x + 2) % 3)].push(stack_list[x].pop())
                        break
            i += 1

    if num is not None and num >= 0:
        s1 = Stack()
        s2 = Stack()
        s3 = Stack()
        for i in range(num-1, -1, -1):
            s1.push(i)
        # print(f"A: {s1}\nB: {s2}\nC: {s3}\n")
        _towers_of_hanoi_bin_counting([s1, s3, s2])
        # print(f"A: {s1}\nB: {s2}\nC: {s3}\n")


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __iter__(self):
        yield self.value
        if self.next is not None:
            yield from self.next

    def __repr__(self):
        return ', '.join(map(repr, self))


class Stack:
    def __init__(self, top=None):
        self.top = top
        self.size = 0

    def __iter__(self):
        return self.top

    def __repr__(self):
        return f"[{self.top}]" if self.top else "[]"

    def push(self, value):
        self.top = Node(value, self.top)
        self.size += 1

    def peek(self):
        return None if self.top is None else self.top.value

    def pop(self):
        value = None
        if self.top is not None:
            value = self.top.value
            self.size -= 1
            self.top = self.top.next
        return value

    def empty(self):
        return True if self.size == 0 else False


n = 15
t = time.time(); print(f"toh({n})", end=""); toh(n); print(f" took {time.time() - t} seconds")
t = time.time(); print(f"towers_of_hanoi({n})", end=""); towers_of_hanoi(n); print(f" took {time.time() - t} seconds")
t = time.time(); print(f"towers_of_hanoi_bin_counting({n})", end=""); towers_of_hanoi_bin_counting(n); print(f" took {time.time() - t} seconds")


