"""
    MOST FREQUENTLY OCCURRING ITEM IN LIST

    Write a method to find the most frequently occurring item/element in a list.

    Example:
         Input = [1, 3, 1, 3, 2, 1]
         Output = 1

    Variations:
        - SEE: find_majority_element.py
        - SEE: majority_element.py
"""


# Dictionary Approach:  Time and space complexity is O(n), where n is the number of items in the list.
def most_freq_item(l):
    d = dict()
    mfi = None
    for i in l:
        d[i] = d.setdefault(i, 0) + 1
        if mfi is None or d[mfi] < d[i]:
            mfi = i
    return mfi


args = [['b', 'a', 'c', 'a', 'a', 'b', 'a', 'a', 'c', 'a'],
        [2, 1, 1, 1, 3, 1, 4, 5, 1, 2, 1, 1, 0, 1, 1, 9, 1],
        [1, 2, 5, 9, 5, 9, 5, 5, 5],
        [3, 1, 7, 1, 3, 7, 3, 7, 1, 7, 7],
        [3, 1, 7, 1, 1, 7, 7, 3, 7, 7, 7],
        [1, 3, 1, 3, 2, 1],
        [1, 3, 1, 3, 2, 1, 3, 3, 2, 1, 3, 3, 3]]

for l in args:
    print(f"most_freq_item({l}):", most_freq_item(l))


