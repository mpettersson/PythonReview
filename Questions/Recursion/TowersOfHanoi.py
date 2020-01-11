"""
    TOWERS OF HANOI


    In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide
    onto any tower.  The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each
    disk sits on top of an even larger one).  You have the following constraints:

        1. Only one disk can be moved at a time.
        2. A disk is slid off the top of one tower onto the next tower.
        3. A disk can only be placed on top of a larger disk.

    Write a program to move the disks from the first tower to the last using stacks.
"""


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self, top=None):
        self.top = top
        self.size = 0

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

    def print_stack(self):
        curr = self.top
        print("[", end="")
        while curr is not None:
            print("", curr.value, end="")
            curr = curr.next
        print(" ]")


def towers_of_hanoi(num):
    if num <= 0:
        raise ValueError
    s1 = Stack()
    s2 = Stack()
    s3 = Stack()
    n = num - 1
    while n >= 0:
        s1.push(n)
        n -= 1
    s1.print_stack()
    s2.print_stack()
    s3.print_stack()
    print()
    move_disks(num, s1, s3, s2)
    s1.print_stack()
    s2.print_stack()
    s3.print_stack()
    print()



def move_disks(n, orig, dest, buff):
    # print("n:", n)
    # orig.print_stack()
    # buff.print_stack()
    # dest.print_stack()
    # print()

    # Base Case
    if n <= 0:
        return

    # Move top n - 1 disks from orig to buffer, using dest as buffer
    move_disks(n - 1, orig, buff, dest)

    # Move top from origin to dest
    # print("moving disk", orig.peek(), "from orig to dest")
    dest.push(orig.pop())

    # Move top n - 1 disks from buffer to dest, using orig as buffer
    move_disks(n - 1, buff, dest, orig)


def towers_of_hanoi_bin_counting(num):
    if num <= 0:
        raise ValueError
    s1 = Stack()
    s2 = Stack()
    s3 = Stack()
    n = num - 1
    while n >= 0:
        s1.push(n)
        n -= 1
    s1.print_stack()
    s2.print_stack()
    s3.print_stack()
    print()
    towers_of_hanoi_using_binary_counting([s1, s2, s3])
    s1.print_stack()
    s2.print_stack()
    s3.print_stack()
    print()


def towers_of_hanoi_using_binary_counting(stack_list):
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


import time
t1 = time.time()
towers_of_hanoi(15)
t2 = time.time()

print("------------")

t3 = time.time()
towers_of_hanoi_bin_counting(15)
t4 = time.time()

print("------------")

print("Recursive TOH took", (t2 - t1), "time.")
print("Bin Counting TOH took", (t4 - t3), "time.")
