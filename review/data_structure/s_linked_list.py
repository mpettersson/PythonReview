class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return repr(self.value)


class LinkedList:

    def __init__(self):
        self.head = None;

    def __len__(self):
        curr = self.head
        counter = 0
        while curr is not None:
            curr = curr.next
            counter += 1
        return counter

    def remove(self, value):
        curr = self.head
        prev = None
        while curr and curr.value != value:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        curr = self.head
        next_node = None
        prev_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node

    def find(self, value):
        curr = self.head
        while curr and curr.value != value:
            curr = curr.next
        return curr

    def add_first(self, value):
        curr = Node(value)
        curr.next = self.head
        self.head = curr

    def add(self, value):
        new_node = Node(value)
        curr = self.head
        if self.head is None:
            self.head = new_node
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def print_linked_list(self):
        curr = self.head
        print("[", end="")
        while curr is not None:
            print("", curr.value, end="")
            curr = curr.next
        print(" ]")


my_ll = LinkedList()

print("my_ll.add(\"B\"):"); my_ll.add("B")
print("my_ll.add(\"C\"):"); my_ll.add("C")
print("my_ll.add(\"D\"):"); my_ll.add("D")
print("my_ll.add(\"E\"):"); my_ll.add("E")
print("my_ll.add(\"F\"):"); my_ll.add("F")
print("my_ll.add(\"G\"):"); my_ll.add("G")
print()

my_ll.print_linked_list()
print("len(my_ll):", len(my_ll), "\n")

print("my_ll.add_first(\"A\"):"); my_ll.add_first("A")
my_ll.print_linked_list()
print("len(my_ll):", len(my_ll), "\n")


print("my_ll.remove(\"A\")"); my_ll.remove("A")
my_ll.print_linked_list()
print("len(my_ll):", len(my_ll), "\n")

print("my_ll.reverse()"); my_ll.reverse()
my_ll.print_linked_list()
print("len(my_ll):", len(my_ll), "\n")

print("my_ll.remove(\"E\")"); my_ll.remove("E")
my_ll.print_linked_list()
print("len(my_ll):", len(my_ll), "\n")

print("my_ll.remove(\"B\")"); my_ll.remove("B")
my_ll.print_linked_list()
print("len(my_ll):", len(my_ll), "\n")
