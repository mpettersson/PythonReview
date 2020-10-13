"""
    COMPUTE AN OPTIMUM ASSIGNMENT OF TASKS (EPI 18.1)

    We consider the problem of assigning tasks to workers.  Each worker must be assigned exactly two tasks.  Each task
    takes a fixed amount of time.  Tasks are independent, i.e., there are no constraints of the form 'Task 4 cannot
    start before Task 3 is completed.'  Any task can be assigned to any worker.

    Design an algorithm that takes as input a set of tasks and returns an optimum assignment.

    Example:
        Input = [5, 2, 1, 6, 4, 4]
        Output = 8  # or, max((5 + 2), (1 + 6), (4 + 4))
"""
import math


# Naive/Brute Force Approach:  This very naive brute force approach would be to enumerate all possible sets of pairs.
# The number of sets is (n choose 2) * (n-2 choose 2) * (n-4 choose 2) * ... * (4 choose 2) * (2 choose 2) which is
# equal to (n!)/(2**(n/2)), where n is the number of tasks.
def optimum_assignment_naive(l):

    def gen_pairs_sets(l):
        res = []
        if len(l) > 0:
            if len(l) is 2:
                return [[(l.pop(), l.pop())]]
            h = l.pop(0)
            for i in range(len(l)):
                pairs = gen_pairs_sets(l[:i] + l[i+1:])
                for p in pairs:
                    p.append((h, l[i]))
                if p not in res:
                    res.extend(pairs)
        return res

    if l is not None and len(l) > 1 and len(l) % 2 is 0:
        sets = gen_pairs_sets(l[:])
        res = []
        min_max_sum = math.inf
        for pairs in sets:
            curr_len = max(map(sum, pairs))
            if curr_len < min_max_sum:
                res = pairs
                min_max_sum = curr_len
        return min_max_sum, res


# Greedy Approach:  Sort the list, then construct pairs via popping the first and last value.  Time complexity is
# O(n * log(n)), where n is the number of element in the list.  Space complexity is O(n), where n is the number of
# elements in the list (this could be reduced to O(1) if the pairs were not returned).
def optimum_assignment(l):
    if l is not None and len(l) > 1 and len(l) % 2 is 0:
        ls = sorted(l)
        pairs = []
        while ls:
            pairs.append((ls.pop(0), ls.pop()))
        return max(map(sum, pairs)), pairs


lists = [[5, 2, 1, 6, 4, 4],
         [8, 1, 9, 10],
         [1, 1, 6, 9, 1, 3, 10, 10, 0, 10],
         []]

for l in lists:
    print(f"l: {l}")
    print(f"optimum_assignment_naive(l): {optimum_assignment_naive(l)}")
    print(f"optimum_assignment(l): {optimum_assignment(l)}")
    print()


