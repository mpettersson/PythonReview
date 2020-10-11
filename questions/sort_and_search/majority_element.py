"""
    MAJORITY ELEMENT (CCI 17.10)

    A majority element is an element that makes up more than half of the items in a list.  Given a list, find the
    majority element, if there is no majority element, return None.

    Do this in O(N) time and O(1) space.

    Example
        Input:  [1, 2, 5, 9, 5, 9, 5, 5, 5]
        Output: 5

    NOTE: Running once to find a possible majority element, and a second run to validate fits the constraints (and is
    what needs to happen)...

    Variations:
        - SEE: find_majority_element.py (same question, different book).
        - SEE: most_frequent_item_in_list.py
"""


# Invariant Approach:  The invariant here is that there exists a majority element.  Given a majority element m and n
# entries, by definition m/n > 1/2.  This holds both for m/(n-2) > 1/2 and (m-1)/(n-1) > 1/2.  Time complexity is O(n),
# where n is the number of elements in the list.  Space complexity is O(1).
def find_majority_element(l):

    def _get_candidate(l):
        majority = 0
        count = 0
        for i in l:
            if count == 0:  # No majority element in previous set.
                majority = i
            if i == majority:
                count += 1
            else:
                count -= 1
        return majority

    def _validate(l, majority):
        count = 0
        for i in l:
            if i == majority:
                count += 1
        return count > len(l) // 2

    if l is not None:
        candidate = _get_candidate(l)
        return candidate if _validate(l, candidate) else None


args = [['b', 'a', 'c', 'a', 'a', 'b', 'a', 'a', 'c', 'a'],
        [2, 1, 1, 1, 3, 1, 4, 5, 1, 2, 1, 1, 0, 1, 1, 9, 1],
        [1, 2, 5, 9, 5, 9, 5, 5, 5],
        [3, 1, 7, 1, 3, 7, 3, 7, 1, 7, 7],
        [3, 1, 7, 1, 1, 7, 7, 3, 7, 7, 7],
        [1, 3, 1, 3, 2, 1],
        [1, 3, 1, 3, 2, 1, 3, 3, 2, 1, 3, 3, 3]]

for a in args:
    print(f"find_majority_element({a}): {find_majority_element(a)}")


