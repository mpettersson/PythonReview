"""
    FIND THE MAJORITY ELEMENT (EPI 18.5)

    Several applications require identification of elements in a sequence which occur more than a specified fraction of
    the total number of elements in the sequence.  For example, we may want to identify the users using excessive
    network bandwidth or IP addresses originating the most Hypertext Transfer Protocol (HTTP) requests.  Here we
    consider a simplified version of this problem.

    You are reading a sequence of strings.  You know a priori that MORE THAN HALF of the strings are repetitions of a
    single string (the 'majority element') but the positions where the majority element occurs are unknown.  Write a
    program that makes a single pass over the sequence and identifies the majority element.

    Example:
        Input = ['b', 'a', 'c', 'a', 'a', 'b', 'a', 'a', 'c', 'a']
        Output = 'a'

    Variations:
        - SEE: majority_element.py for a more complete solution (i.e., VERIFY the selected element...)
        - SEE: most_frequent_item_in_list.py
"""


# Invariant Approach:  The invariant here is that there exists a majority element.  Given a majority element m and n
# entries, by definition m/n > 1/2.  This holds both for m/(n-2) > 1/2 and (m-1)/(n-1) > 1/2.  Time complexity is O(n),
# where n is the number of elements in the iterable.  Space complexity is O(1).
def find_majority_element(iterable):
    if iterable is not None:
        i = next(iterable)
        candidate = None
        candidate_count = 0
        while i is not None:
            if candidate_count is 0:
                candidate = i
                candidate_count = 1
            elif candidate == i:
                candidate_count += 1
            else:
                candidate_count -= 1
            i = next(iterable, None)
        return candidate


args = [['b', 'a', 'c', 'a', 'a', 'b', 'a', 'a', 'c', 'a'],
        [2, 1, 1, 1, 3, 1, 4, 5, 1, 2, 1, 1, 0, 1, 1, 9, 1],
        [1, 2, 5, 9, 5, 9, 5, 5, 5],
        [3, 1, 7, 1, 3, 7, 3, 7, 1, 7, 7],          # NO Majority Element; but gets lucky and finds most frequent.
        [3, 1, 7, 1, 1, 7, 7, 3, 7, 7, 7],
        [1, 3, 1, 3, 2, 1],                         # NO Majority Element; WRONG...
        [1, 3, 1, 3, 2, 1, 3, 3, 2, 1, 3, 3, 3]]


for a in args:
    print(f"find_majority_element(iter({a})): {find_majority_element(iter(a))}")


