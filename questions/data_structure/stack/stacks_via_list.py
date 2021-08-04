"""
    STACKS VIA LIST (CCI 3.1: THREE IN ONE,
                     50CIQ 13: N STACKS)

    Given a number of stacks, n (integer), and a total available size, s (integer), implement n stacks using a (single)
    list of size s to store all the data/values pushed to any of the n stacks.  All stacks must maintain the condition
    that a (single) stack becomes full only when the entire list (of size s) is full.  Note that other data structures
    (or lists) may used to aid in the stacks logistics (but not to store stack values).

"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What data type will the stack contain?  (This may affect some languages more than others.)
#   - What do you want to happen when a push occurs on a full stack?
#   - What do you want to happen when a pop occurs on an empty stack?
#   - What methods do you want implemented?  (Define the methods signatures, if time allows then add/finish logic.)


# WRONG APPROACH: Naive Fixed Division
#
# Simply divide the array into three equal parts.
#
# NOTE: This DOES NOT maintain the condition that "a stack becomes full only when the entire list (of size s) is full"!
class StacksViaListWrong:
    def __init__(self, num_stacks=3, size=10):
        if not isinstance(num_stacks, int) or not isinstance(size, int) or num_stacks < 1 or size < 1:
            raise TypeError(f"FixedMultiStack arguments must be ints greater than zero.")
        self.num_stacks = num_stacks
        self.stack_capacity = size // num_stacks
        self.values = [None] * size
        self.sizes = [0] * self.num_stacks

    def __repr__(self):
        return "\n\tvalues: " + repr(self.values)

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


# (COMPLEX) APPROACH:  Flexible Divisions (StacksViaListComplex)
#
# Allow each stack to be flexible in size, and use the list as a circular list.  Is composed of two classes:
#   StackInfo - Contains the logistic/management information for a single stack.
#   StacksViaListComplex - Class that contains the (single) list with all stack values as well as StackInfo objects.
class StackInfo:
    """This Class contains the logistic/management information for a single stack."""

    def __init__(self, start, capacity):
        self.start = start
        self.capacity = capacity            # Can change.
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
        return repr({"start": self.start,
                     "capacity": self.capacity,
                     "size": self.size})


# (COMPLEX) APPROACH CONTINUED:  Flexible Divisions (StacksViaListComplex)
class StacksViaListComplex:
    def __init__(self, num_stacks, size):
        if not isinstance(num_stacks, int) or not isinstance(size, int) or num_stacks < 1 or size < 1:
            raise TypeError(f"MultiStack arguments must be ints greater than zero.")
        self.info = []
        self.values = [None] * size
        for i in range(num_stacks):
            default_size = size // num_stacks
            if i == 0:
                default_size += size % num_stacks
            self.info.append(StackInfo(default_size * i, default_size))

    def __repr__(self):
        return "\n\tinfo: " + repr(self.info) + "\n\tvalues: " + repr(self.values)

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

    def shift(self, stack_num):
        """Shifts items in stack over by one element.
           If available capacity, then shrink stack by one element.  If not, then shift the next stack over too."""
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

    def adjust_index(self, index):
        """Adjust index to be within range of 0 to len - 1."""
        return index % len(self.values)

    def next_index(self, index):
        return self.adjust_index(index + 1)

    def previous_index(self, index):
        return self.adjust_index(index - 1)


# (SIMPLE) APPROACH:  Via Pointers (StacksViaList)
#
# This approach simply interleaves the stacks data (so the stacks may be non-contagious in the list) via a minimal set
# of pointers which track the state of the stacks/list.  The stacks are maintained via:
#   Top Of Stack List:  Length n, where each index points to the corresponding stacks top in the list, or -1 if empty.
#   Stack Data:         The actual list, of length s, which contains the values on the stacks.
#   Next Index:         Length s, where indices point to either the:
#                           Next available list index, if corresponds to a stacks top, or a unused index.
#                           Previous (or last used) index for the corresponding stack.
#   Next Available:     The first empty index in the list.
#
# SEE: Console output for printed representation of the pointers values.
#
# NOTE: This approach interleaves stacks values!
class StacksViaList:
    def __init__(self, num_stacks, capacity):
        if not isinstance(num_stacks, int) or not isinstance(capacity, int) or num_stacks < 1 or capacity < 1:
            raise TypeError(f"num_stacks and capacity must be ints greater than zero.")
        self.top_of_stack = [-1 for _ in range(num_stacks)]             # Top Index (Per Stack)
        self.stack_data = [None for _ in range(capacity)]               # Actual Data/Values
        self.next_index = [i for i in range(1, capacity)] + [-1]        # Next (All) & Previous (Per Stack) Pointer.
        self.next_available = 0                                         # Next Index, -1 can serve as a full flag.

    def __repr__(self):
        return "\n\ttop_of_stack: " + repr(self.top_of_stack) + "\n\tstack_data: " + repr(self.stack_data) + "\n\tnext_index: " + repr(self.next_index) + "\n\tnext_available: " + repr(self.next_available)

    def push(self, stack, value):
        if not isinstance(stack, int) or stack < 0 or stack >= len(self.top_of_stack):
            raise TypeError(f"Invalid stack value.")
        if self.next_available < 0:
            raise TypeError(f"All stacks full.")
        curr_index = self.next_available
        self.next_available = self.next_index[curr_index]
        self.stack_data[curr_index] = value
        self.next_index[curr_index] = self.top_of_stack[stack]
        self.top_of_stack[stack] = curr_index

    def pop(self, stack):
        if not isinstance(stack, int) or stack < 0 or stack >= len(self.top_of_stack):
            raise TypeError(f"Invalid stack value.")
        if self.top_of_stack[stack] < 0:
            raise IndexError(f"Pop from empty stack.")
        curr_index = self.top_of_stack[stack]
        result = self.stack_data[curr_index]
        self.stack_data[curr_index] = None      # Needed for correct __repr__ state/representation.
        self.top_of_stack[stack] = self.next_index[curr_index]
        self.next_index[curr_index] = self.next_available
        self.next_available = curr_index
        return result

    def peek(self, stack):
        if not isinstance(stack, int) or stack < 0 or stack >= len(self.top_of_stack):
            raise TypeError(f"Invalid stack value.")
        if self.top_of_stack[stack] < 0:
            raise IndexError(f"Peek from empty stack.")
        return self.stack_data[self.top_of_stack[stack]]

    def is_full(self):
        return self.next_available < 0

    def is_empty(self):
        return all([x < 0 for x in self.top_of_stack])


classes = [StacksViaListWrong,
           StacksViaListComplex,
           StacksViaList]

for cls in classes:
    print(f"===== {cls.__name__} Class =====")
    stacks = cls(3, 10)
    print(f"stacks = {cls.__name__}(3, 10)")
    print(f"stacks: {stacks}")

    # Push and pop from the third stack:
    print(f"stacks.push(2, 's2,v0'): {stacks.push(2, 's2,v0')}")
    print(f"stacks: {stacks}")
    print(f"stacks.pop(2): {stacks.pop(2)!r}")
    print(f"stacks: {stacks}")

    # Push 3 values to the first stack:
    for i in range(3):
        print(f"stacks.push(0, 's0,v{i}'): {stacks.push(0, 's0,v' + str(i))}")
    print(f"stacks: {stacks}")

    # Try pushing 7 values to the second stack:
    try:
        for i in range(7):
            print(f"stacks.push(1, 's1,v{i}'): ", end="")
            print(f"{stacks.push(1, 's1,v' + str(i))}")
    except Exception as e:
        print(f"Exception Caught: {e}")
    print(f"stacks: {stacks}")

    # Try pushing to each of the stacks.
    try:
        for i in range(1, 3):
            print(f"stacks.push(2, 's1,v{i}'): ", end="")
            print(f"{stacks.push(2, 's1,v' + str(i))}")
    except Exception as e:
        print(f"Exception Caught: {e}")
    print(f"stacks: {stacks}")

    # Try popping one off of each of the stacks:
    try:
        for i in range(3):
            print(f"stacks.pop({i}): ", end="")
            print(f"{stacks.pop(i)}")
    except Exception as e:
        print(f"Exception Caught: {e}")
    print(f"stacks: {stacks}")
    print("\n")


