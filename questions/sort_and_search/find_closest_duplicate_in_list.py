"""
    FIND CLOSEST DUPLICATE IN LIST (EPI 13.6: FIND THE NEAREST REPEATED ENTRIES IN AN ARRAY)

    Write a function that returns the distance between the closest (entry) duplicate in a list.

    Example:
         Input = ['she', 'sells', 'seashells', 'by', 'the', 'seashore', 'the', 'shells', 'she', 'sells', 'are',
                  'seashells', 'i’m', 'sure', 'so', 'if', 'she', 'sells', 'seashells', 'on', 'the', 'seashore', 'then',
                  'i’m', 'sure', 'she', 'sells', 'seashore', 'shells']
         Output = ('the', 2)
"""


# APPROACH: Naive/Brute Force
#
# For each element in the list, compare all the following elements to find the nearest duplicate.  Whenever the nearest
# duplicate is found, compare the current duplicates distance to the previous closest duplicate distance, updating if
# necessary.
#
# Time Complexity: O(n**2), where n is the number of elements in the list.
# Space Complexity: O(1).
def find_closest_duplicate_in_list_naive(l):
    if l:
        dup_value = None
        dup_start = None
        dup_end = None
        for i in range(len(l)-1):
            for j in range(i+1, len(l)):
                if l[i] is l[j] and (dup_start is None or dup_end - dup_start > j - i):
                    dup_value = l[i]
                    dup_start = i
                    dup_end = j
                    break
        return dup_value, dup_end - dup_start


# APPROACH: Dictionary/Hash Map Approach
#
# Iterate over the elements in the list, using a dictionary to maintain the elements previous position.  When a new
# element is encountered add its position to the dictionary.  If the element is already in the dictionary (has been
# encountered) compute the distance then compare it with the current best distance.  If the current distance is an
# improvement, update the duplicates value and its distance.
#
# Time Complexity: O(n), where n is the number of elements in the list.
# Space Complexity: O(u), where u is the number of unique elements in the list.
def find_closest_duplicate_in_list(l):
    if l:
        d = {}
        dup_dist = len(l)+1
        dup_value = None
        for i, w in enumerate(l):
            if w not in d:
                d[w] = i
            else:
                if i - d[w] < dup_dist:
                    dup_dist = i - d[w]
                    dup_value = w
                    d[w] = i
        return dup_value, dup_dist



lists = [['she', 'sells', 'seashells', 'by', 'the', 'seashore', 'the', 'shells', 'she', 'sells', 'are', 'seashells',
          'i’m', 'sure', 'so', 'if', 'she', 'sells', 'seashells', 'on', 'the', 'seashore', 'then', 'i’m', 'sure', 'she',
          'sells', 'seashore', 'shells'],
         ['all', 'work', 'and', 'no', 'play', 'makes', 'for', 'no', 'work', 'no', 'fun', 'and', 'no', 'results'],
         [4, 11, 13, 37, 38, 28, 1, 6, 9, 24, 30, 11, 9, 38, 3, 13, 6, 22, 5, 48]]
fns = [find_closest_duplicate_in_list_naive,
       find_closest_duplicate_in_list]

for l in lists:
    print(f"l: {l}\n")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l)}")
    print()


