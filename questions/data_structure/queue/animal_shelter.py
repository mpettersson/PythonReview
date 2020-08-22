"""
    ANIMAL SHELTER (CCI 3.6)

    An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis.  People must
    adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they
    would prefer a dog or a cat (and will receive the oldest animal of that type).  They cannot select which specific
    animal they would like.  Create the data structures to maintain this system and implement operations such as
    enqueue, dequeue_any, dequeue_dog, and dequeue_cat.  You may use the built-in list data structure.
"""
import time


# Two Queue Approach:  Two queues, one for dogs and one for cats, will contain information on the animals (including a
# timestamp when they were enqueued).  This information can then be used when enqueue_any is called.
# Each of the enqueuing/dequeueing calls complete in O(1) time, space complexity of the AnimalShelter is O(n).
class AnimalNode:
    def __init__(self, name, next=None):
        self.name = name
        self.next = next
        self.time = time.time()

    def __repr__(self):
        return f"{repr(self.name)}({self.__class__.__name__})"


class Dog(AnimalNode):
    def __init__(self, name, next=None):
        AnimalNode.__init__(self, name, next)


class Cat(AnimalNode):
    def __init__(self, name, next=None):
        AnimalNode.__init__(self, name, next)


class AnimalShelter:
    def __init__(self, *animals):
        self.f_dog = None
        self.l_dog = None
        self.f_cat = None
        self.l_cat = None
        for (t, n) in animals:
            self.enqueue(t, n)

    def enqueue(self, animal_type, name):
        if animal_type is Dog:
            if not self.f_dog:
                self.f_dog = animal_type(name)
                self.l_dog = self.f_dog
            else:
                self.l_dog.next = animal_type(name)
                self.l_dog = self.l_dog.next
        elif animal_type is Cat:
            if not self.f_cat:
                self.f_cat = animal_type(name)
                self.l_cat = self.f_cat
            else:
                self.l_cat.next = animal_type(name)
                self.l_cat = self.l_cat.next

    def dequeue_any(self):
        if self.f_dog and not self.f_cat or self.f_dog and self.f_cat and self.f_dog.time < self.f_cat.time:
            return self.dequeue_dog()
        elif self.f_cat and not self.f_dog or self.f_dog and self.f_cat and self.f_cat.time < self.f_dog.time:
            return self.dequeue_cat()
        else:
            raise IndexError("dequeue from empty queue")

    def dequeue_cat(self):
        if self.f_cat:
            cat = self.f_cat
            self.f_cat = self.f_cat.next
            return cat
        raise IndexError("dequeue_cat from queue without cats")

    def dequeue_dog(self):
        if self.f_dog:
            dog = self.f_dog
            self.f_dog = self.f_dog.next
            return dog
        raise IndexError("dequeue_dog from queue without dogs")

    def __iter__(self):
        dog = self.f_dog
        cat = self.f_cat
        while cat or dog:
            if (not cat and dog) or (cat and dog and cat.time > dog.time):
                yield dog
                dog = dog.next
            elif (not dog and cat) or (cat and dog and dog.time > cat.time):
                yield cat
                cat = cat.next

    def __repr__(self):
        return f"[{', '.join(map(repr, self))}]"


animal_shelter = AnimalShelter((Dog, 'Winter'), (Cat, 'Popcorn'), (Cat, 'Donut'), (Dog, "Jake"), (Dog, "Mia"))
print(f"animal_shelter: {animal_shelter}")
print(f"animal_shelter.enqueue(Cat, 'Icecream'): {animal_shelter.enqueue(Cat, 'Icecream')}")
print(f"animal_shelter.enqueue(Dog, 'Fido'): {animal_shelter.enqueue(Dog, 'Fido')}")
print(f"animal_shelter: {animal_shelter}")
print(f"animal_shelter.dequeue_cat(): {animal_shelter.dequeue_cat()}")
print(f"animal_shelter: {animal_shelter}")
print(f"animal_shelter.dequeue_any(): {animal_shelter.dequeue_any()}")
print(f"animal_shelter: {animal_shelter}")
print(f"animal_shelter.dequeue_dog(): {animal_shelter.dequeue_dog()}")
print(f"animal_shelter: {animal_shelter}")
print(f"animal_shelter.dequeue_any(): {animal_shelter.dequeue_any()}")
print(f"animal_shelter: {animal_shelter}")
print(f"animal_shelter.dequeue_cat(): {animal_shelter.dequeue_cat()}")
print(f"animal_shelter: {animal_shelter}")
print(f"animal_shelter.dequeue_any(): {animal_shelter.dequeue_any()}")
print(f"animal_shelter: {animal_shelter}")
print(f"animal_shelter.dequeue_any(): {animal_shelter.dequeue_any()}")
print(f"animal_shelter: {animal_shelter}")
print(f"animal_shelter.enqueue(Cat, 'Icecream'): {animal_shelter.enqueue(Cat, 'Icecream')}")
print(f"animal_shelter: {animal_shelter}")
print(f"animal_shelter.dequeue_any(): {animal_shelter.dequeue_any()}")
print(f"animal_shelter: {animal_shelter}")
try:
    print(f"animal_shelter.dequeue_any(): {animal_shelter.dequeue_any()}")
except IndexError as e:
    print("IndexError:", e.args)
try:
    print(f"animal_shelter.dequeue_cat(): {animal_shelter.dequeue_cat()}")
except IndexError as e:
    print("IndexError:", e.args)
try:
    print(f"animal_shelter.dequeue_dog(): {animal_shelter.dequeue_dog()}")
except IndexError as e:
    print("IndexError:", e.args)


