"""
    WORD DISTANCE

    You have a large text file containing words.  Given any two words, find the shortest distance (in terms of number of
    words) between them in the file.  If the operation will be repeated many times for the same file (but different
    words), can you optimize your solution?

"""
import re


# Approach 1:  Naively--Read once and compare, time is O(N) where N is the number of words in the list, space is O(1).
def word_distance(word_list, word_one, word_two):
    best = LocationPair(-1, -1)
    current = LocationPair(-1, -1)
    for i, w in enumerate(word_list):
        if w == word_one:
            current.location_one = i
            best.update_with_min(current)
        elif w == word_two:
            current.location_two = i
            best.update_with_min(current)
    return best.distance(), (best.location_one, best.location_two)


class LocationPair:
    def __init__(self, location_one=-1, location_two=-1):
        self.location_one = location_one
        self.location_two = location_two

    def set_locations(self, location_one, location_two):
        self.location_one = location_one
        self.location_two = location_two

    def distance(self):
        return abs(self.location_one - self.location_two)

    def is_valid(self):
        return self.location_one >= 0 and self.location_two >= 0

    def update_with_min(self, location_pair):
        if location_pair.is_valid() and (not self.is_valid() or location_pair.distance() < self.distance()):
            self.location_one = location_pair.location_one
            self.location_two = location_pair.location_two


# Approach 2:  Use a dictionary (word -> list of locations) to prevent multiple reads...
# Time complexity to create the dict is O(N), where N is the number of words.
# Time complexity to find closest pair is O(A + B), where A and B are the number of word_one and word_two occurrences.
def word_distance_via_dict(word_dict, word_one, word_two):
    if word_one not in word_dict or word_two not in word_dict:
        return None
    locations_one = word_dict[word_one]
    locations_two = word_dict[word_two]
    return find_min_distance_pair(locations_one, locations_two)


def find_min_distance_pair(list_one, list_two):
    if list_one is None or list_two is None or len(list_one) == 0 or len(list_two) == 0:
        return None

    index_one = 0
    index_two = 0
    best = LocationPair(list_one[0], list_two[0])
    current = LocationPair(list_one[0], list_two[0])

    while index_one < len(list_one) and index_two < len(list_two):
        current.set_locations(list_one[index_one], list_two[index_two])
        best.update_with_min(current)  # If shorter, update values.
        if current.location_one < current.location_two:
            index_one += 1
        else:
            index_two += 1

    return best.distance(), (best.location_one, best.location_two)


def create_word_dict(word_list):
    word_dict = dict()
    for i, w in enumerate(word_list):
        if w in word_dict:
            word_dict[w].append(i)
        else:
            word_dict[w] = [i]
    return word_dict


zen = "Beautiful is better than ugly.  Explicit is better than implicit.  Simple is better than complex.  Complex is " \
      "better than complicated.  Flat is better than nested.  Sparse is better than dense.  Readability counts.  " \
      "Special cases are not special enough to break the rules.  Although practicality beats purity.  Errors should " \
      "never pass silently.  Unless explicitly silenced.  In the face of ambiguity, refuse the temptation to guess.  " \
      "There should be one, and preferably only one, obvious way to do it.  Although that way may not be obvious at " \
      "first unless you are Dutch.  Now is better than never.  Although never is often better than right now.  If " \
      "the implementation is hard to explain, it is a bad idea.  If the implementation is easy to explain, " \
      "it may be a good idea.  Namespaces are one honking great idea, let us do more of those!"
zen_list = re.sub(r"\.|,|!", "", zen.lower()).split()
word_one = "it"
word_two = "is"
word_three = "asinine"
print("zen:", zen)
print("zen_list:", zen_list)
print("word_one:", word_one)
print("word_two:", word_two)
print("word_three:", word_three)
print()

print("word_distance(zen_list, word_one, word_two):", word_distance(zen_list, word_one, word_two))
print("word_distance(zen_list, word_one, word_three):", word_distance(zen_list, word_one, word_three))
print("word_distance(zen_list, word_two, word_three):", word_distance(zen_list, word_two, word_three))
print()

word_dict = create_word_dict(zen_list)
print("word_distance_via_dict(word_dict, word_one, word_two):", word_distance_via_dict(word_dict, word_one, word_two))
print("word_distance_via_dict(word_dict, word_two, word_three):", word_distance_via_dict(word_dict, word_two, word_three))
print("word_distance_via_dict(word_dict, word_three, word_one):", word_distance_via_dict(word_dict, word_three, word_one))


