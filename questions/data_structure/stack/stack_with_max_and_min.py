"""
    STACK WITH MIN AND MAX (CCI 3.2: STACK MIN,
                            50CIQ 31: MAX STACKS)

    Create a stack class which, in addition to push and pop, have the functions min and max, which returns the minimum
    and maximum elements respectively?  Push, pop and min should all operate in O(1) time.
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Can a Python list be used, implement it, or assume it is created (if created what are the names)?
#   - What other stack methods should be created (size, is_empty, etc.)?
#   - What data types will the stack contain (if not ints what type of max/min function should be used)?


# NOTE: TWO of the following three solutions use python lists, in a first in last out (FILO) order, as a replacement for
#       node/stack classes to (minimally) cut down on the length/complexity of the code.  In an interview you would want
#       to ask the interviewer if this substitution was acceptable.


# APPROACH: (Naive) List As Stack Of Tuples (Value, Min, Max)
#
# This less efficient solution simply maintains a list of 3-tuples (value, curr_max, curr_min), pushing and popping from
# at the end of the list to emulate a stack.  Please note that in a sitiuation where the max/min value was first pushed,
# many duplicates would exist in a long list (this isn't good).
#
# Time Complexity: SEE methods below.
# Space Complexity: O(3n), which reduces to O(n), where n is the number of elements in the stack.
class ListAsStackWithMaxMinNaive:
    def __init__(self, *args):
        self.l = []                                     # (value, curr_max, curr_min) list, push/pop at END.
        for i in args:
            self.push(i)

    # Time Complexity: O(1).
    def push(self, value):
        max_value = min_value = value
        if self.l:
            min_value = min(min_value, self.l[0][2])
            max_value = max(self.l[0][1], max_value)
        self.l.append((value, max_value, min_value))

    # Time Complexity: O(1).
    def pop(self):
        if self.l:
            return self.l.pop()[0]
        raise IndexError("Empty Stack")

    # Time Complexity: O(1).
    def peek(self):
        if self.l:
            return self.l[-1][0]
        raise IndexError("Empty Stack")

    # Time Complexity: O(1).
    def min(self):
        if self.l:
            return self.l[-1][1]
        raise IndexError("Empty Stack")

    # Time Complexity: O(1).
    def max(self):
        if self.l:
            return self.l[-1][2]
        raise IndexError("Empty Stack")

    def __repr__(self):
        return f"(Top){list(reversed(self.l))}"

    def __len__(self):
        return len(self.l)


# APPROACH: List As Stack With Separate Max/Min
#
# This approach uses two additional lists (as stacks) to maintain the maximum and minimum values seen.  Whenever a value
# greater than or equal to the current max value is pushed, the value is also added to the max stack.  Whenever a value
# less than or equal to the current min value is pushed, the value is also added to the min stack.  Whenever a pop is
# initiated, the popped value (which will be returned) will be compared to the heads of the max and min stacks; if it
# matches then the respective stacks will also be popped.
#
# Time Complexity: SEE Below.
# Space Complexity: O(n), where n is the number of elements in the stack.
class ListAsStackWithMaxMin:
    # Time Complexity: O(n), where n is the number of arguments.
    def __init__(self, *args):
        self.stack = []         # All Stack Values; End of list is the top of the stack.
        self.max_s = []         # Max Values; End of list is the top of the stack.
        self.min_s = []         # Min Values; End of list is the top of the stack.
        for i in args:
            self.push(i)

    # Time Complexity: O(1).
    def push(self, value):
        if not self.min_s or value <= self.min_s[-1]:
            self.min_s.append(value)
        if not self.max_s or value >= self.max_s[-1]:
            self.max_s.append(value)
        self.stack.append(value)

    # Time Complexity: O(1).
    def pop(self):
        if self.stack:
            if self.min_s[-1] == self.stack[-1]:
                self.min_s.pop()
            return self.stack.pop()
        raise IndexError("Empty Stack")

    # Time Complexity: O(1).
    def min(self):
        if self.min_s:
            return self.min_s[-1]
        raise IndexError("Empty Stack")

    # Time Complexity: O(1).
    def max(self):
        if self.max_s:
            return self.max_s[-1]
        raise IndexError("Empty Stack")

    # Time Complexity: O(1).
    def peek(self):
        if self.stack:
            return self.stack[-1]
        raise IndexError("Empty Stack")

    def __repr__(self):
        return f"Stack: (Top){list(reversed(self.stack))}\tMax Stack: (Top){list(reversed(self.max_s))}\tMin Stack: (Top){list(reversed(self.min_s))}"

    def __len__(self):
        return len(self.stack)


# APPROACH: Linked List As Stack With Max/Min Pointers
#
# This approach creates a Node and a Stack (StackWithMaxMin) class.  The Node class, in addition to the value and next
# instance variables, contains a my_max and my_min instance variable that point to the nodes with maximum and minimum
# values.  The only difference in the Stack (StackWithMaxMin) class are; the additional max and min methods (that simply
# check top is valid then returns the values for the my_max and my_min pointers), and the assignment of the new nodes
# max/min pointers when a push occurs (this is a short comparison to the previous tops my_max/my_min pointers values).
#
# Time Complexity: SEE Below.
# Space Complexity: O(n), where n is the number of elements in the stack.
class Node:
    def __init__(self, value, next=None, my_max=None, my_min=None):
        self.value = value
        self.next = next
        self.my_max = my_max
        self.my_min = my_min

    def __iter__(self):
        yield self.value
        if self.next:
            yield from self.next

    def __repr__(self):
        return repr(self.value) + " ⟶ " + (repr(self.next) if self.next else "None")


class StackWithMaxMin:
    def __init__(self, *args):
        self.top = None
        for e in args:
            self.push(e)

    def push(self, value):
        node = Node(value, self.top)
        node.my_max = node if self.top is None or value > self.top.my_max.value else self.top.my_max.my_max
        node.my_min = node if self.top is None or value < self.top.my_min.value else self.top.my_min.my_min
        self.top = node

    def pop(self):
        if self.top:
            result = self.top.value
            self.top = self.top.next
            return result
        raise IndexError

    def peek(self):
        if self.top:
            return self.top.value
        raise IndexError

    def max(self):
        if self.top:
            return self.top.my_max.value
        raise IndexError

    def min(self):
        if self.top:
            return self.top.my_min.value
        raise IndexError

    def __len__(self):
        node = self.top
        counter = 0
        while node:
            node = node.next
            counter += 1
        return counter

    def __repr__(self):
        return "(Top) " + repr(self.top)


classes = [ListAsStackWithMaxMinNaive,
           ListAsStackWithMaxMin,
           StackWithMaxMin]

for cls in classes:
    c_name = str.lower(cls.__name__)
    print(f"\n{c_name} = {cls.__name__}(0, 2, 5)"); c = cls(0, 2, 5)
    print(f"repr({c_name}): {repr(c)}")
    for value in [-1, 5, -42, 42]:
        print(f"{c_name}.max():{c.max()}\n{c_name}.min(): {c.min()}")
        print(f"{c_name}.push({value})"); c.push(value)
    print(f"repr({c_name}): {repr(c)}")
    for _ in range(len(c) // 2):
        print(f"{c_name}.pop(): {c.pop()}")
    print(f"len({c_name}): {len(c)}")
    print(f"repr({c_name}): {repr(c)}")
    print(f"{c_name}.max():{c.max()}\n{c_name}.min(): {c.min()}")
    print()


