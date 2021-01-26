"""
    STACKS VIA LIST (CCI 3.1: THREE IN ONE,
                     50CIQ 13: N STACKS)

    Write a class, which accepts a size s and a number n, then creates n stacks out of a single list of size s.  All
    values pushed (to any stack) must be stored in the list, however, other data structures/lists may used for other
    purposes.  A stack is full only when the entire list (of size s) is full.

"""


# Fixed Division Approach: Simply divide the array into three equal parts.
class FixedMultiStack:
    def __init__(self, stack_size, number_of_stacks=3):
        self.number_of_stacks = number_of_stacks
        self.stack_capacity = stack_size
        self.values = [None] * (self.stack_capacity * self.number_of_stacks)
        self.sizes = [0] * self.number_of_stacks

    def __repr__(self):
        return repr(self.values)

    def push(self, stack_num, value):
        if self.full(stack_num):
            raise IndexError(f"stack {stack_num} is full")
        self.sizes[stack_num] += 1                          # Increase stack pointer.
        self.values[self.index_of_top(stack_num)] = value   # Update top value.

    def pop(self, stack_num):
        if self.empty(stack_num):
            raise IndexError(f"stack {stack_num} is empty")
        top_index = self.index_of_top(stack_num)
        value = self.values[top_index]                      # Get top value.
        self.values[top_index] = None                       # Clear.
        self.sizes[stack_num] -= 1                          # Update size.
        return value

    def peek(self, stack_num):
        if self.empty(stack_num):
            raise IndexError(f"stack {stack_num} is empty")
        return self.values[self.index_of_top(stack_num)]

    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_capacity
        size = self.sizes[stack_num]
        return offset + size - 1

    def full(self, stack_num):
        return self.sizes[stack_num] == self.stack_capacity

    def empty(self, stack_num):
        return self.sizes[stack_num] == 0


# Flexible Divisions Approach:  Allow each stack to be flexible in size, and use the list as a circular list.
class StackInfo:
    def __init__(self, start, capacity):
        self.start = start
        self.capacity = capacity
        self.size = 0

    # Check if index in full list is within stack boundaries.  The stack can wrap around to the start of list.
    def is_within_stack_cap(self, index, length):
        if 0 <= index < length:
            contiguous_index = index + length if index < self.start else index  # If it wrapped around.
            end = self.start + self.capacity
            return self.start <= contiguous_index < end
        return False

    def last_capacity_index(self, adjust_index):
        return adjust_index(self.start + self.capacity - 1)

    def last_element_index(self, adjust_index):
        return adjust_index(self.start + self.size - 1)

    def full(self):
        return self.size == self.capacity

    def empty(self):
        return self.size == 0

    def __repr__(self):
        return repr({"start": self.start, "capacity": self.capacity, "size": self.size})


class MultiStack:
    def __init__(self, number_of_stacks, default_size):
        self.info = []
        for i in range(number_of_stacks):
            self.info.append(StackInfo(default_size * i, default_size))
        self.values = [None] * (number_of_stacks * default_size)

    def __repr__(self):
        return repr(self.info) + repr(self.values)

    def push(self, stack_num, value):
        if self.all_stacks_are_full():
            raise IndexError(f"all stacks are full")
        stack = self.info[stack_num]
        if stack.full():
            self.expand(stack_num)
        stack.size += 1
        self.values[stack.last_element_index(self.adjust_index)] = value

    def pop(self, stack_num):
        stack = self.info[stack_num]
        if stack.empty():
            raise IndexError(f"stack[{stack_num}] is full")
        value = self.values[stack.last_element_index(self.adjust_index)]
        self.values[stack.last_element_index(self.adjust_index)] = None     # Clear
        stack.size -= 1
        return value

    def peek(self, stack_num):
        stack = self.info[stack_num]
        return self.values[stack.last_element_index(self.adjust_index)]

    # Shifts items in stack over by one element.  If available capacity, then shrink stack by one element.  If not, then
    # shift the next stack over too.
    def shift(self, stack_num):
        # print(f"/// Shifting {stack_num}")
        stack = self.info[stack_num]
        if stack.size >= stack.capacity:                                # If this stack is at full capacity:
            next_stack = (stack_num + 1) % len(self.info)
            self.shift(next_stack)                                      # Move next stack over by one.
            stack.capacity += 1                                         # Claim index (that next stack lost).
        index = stack.last_capacity_index(self.adjust_index)
        while stack.is_within_stack_cap(index, len(self.values)):       # Shift all elements in stack over by one.
            self.values[index] = self.values[self.previous_index(index)]
            index = self.previous_index(index)
        self.values[stack.start] = None                                 # Clear item.
        stack.start = self.next_index(stack.start)                      # Move start.
        stack.capacity -= 1                                             # Update capacity.

    # Expand stack by shifting over other stacks.
    def expand(self, stack_num):
        self.shift((stack_num + 1) % len(self.info))
        self.info[stack_num].capacity += 1

    def all_stacks_are_full(self):
        return self.number_of_elements() == len(self.values)

    def number_of_elements(self):
        size = 0
        for i in self.info:
            size += i.size
        return size

    # Adjust index to be within range of 0 to len - 1.
    def adjust_index(self, index):
        return index % len(self.values)

    def next_index(self, index):
        return self.adjust_index(index + 1)

    def previous_index(self, index):
        return self.adjust_index(index - 1)


fixed_multi_stacks = FixedMultiStack(5)
for i in range(3):
    for j in range(i + 2):
        print(f"fixed_multi_stacks.push({i}, {str(i) + str(j)})")
        fixed_multi_stacks.push(i, str(i) + str(j))
print(f"fixed_multi_stacks: {fixed_multi_stacks}")
for i in range(3):
    print(f"fixed_multi_stacks.peek({i}): {fixed_multi_stacks.peek(i)}")
    print(f"fixed_multi_stacks.pop({i}): {fixed_multi_stacks.pop(i)}")
print(f"fixed_multi_stacks: {fixed_multi_stacks}")
print()

multi_stacks = MultiStack(3, 5)
for i in range(3):
    print(f"multi_stacks.push(2, {'2'+str(i)}): {multi_stacks.push(2, '2'+str(i))}")

for i in range(8):
    print(f"multi_stacks.push(1, {'1' + str(i)}): {multi_stacks.push(1, '1' + str(i))}")
print(f"multi_stacks: {multi_stacks}")


