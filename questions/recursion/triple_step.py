"""
    TRIPLE STEP (CCI 8.1)

    A child is running up a staircase with N steps and can hop either 1 step, 2 steps, or 3 steps at a time.
    Implement a method to count the number of ways a child can run up the staircase.

    Example:
        Input = 5
        Output = 13

    NOTE: Because the options are 1 OR 2 OR 3 steps, you will add; however, if the options were _ AND _ AND _, you would
    multiply (the recursive results).

    NOTE: Variations of this question include:
            - How many ways are there to climb N steps?
            - How many ways are there to climb N steps, jumping 1, 3, or 5 steps at a time?
"""


# Recursive Approach: O(3 ** n) time!!!
def rec_triple_step(n):
    if n is not None and n >= 0:
        if 0 <= n <= 2:
            return n
        if n is 3:
            return 4
        return rec_triple_step(n - 1) + rec_triple_step(n - 2) + rec_triple_step(n - 3)


# Top Down Dynamic Programming/Memoization Approach: O(n) runtime, O(n) space.
def top_down_triple_step(n):
    if n is not None and n >= 0:
        l = [None] * (n + 1)
        return memo_triple_step(n, l)


def memo_triple_step(n, l):
    if 0 <= n <= 2:
        return n
    if n is 3:
        return 4
    if l[n] is None:
        l[n] = memo_triple_step(n - 1, l) + memo_triple_step(n - 2, l) + memo_triple_step(n - 3, l)
    return l[n]


# Bottom Up Dynamic Programming/Tabulation with a list Approach: O(n) runtime, O(n) space.
def tabulation_with_list_triple_step(n):
    if n is not None and n >= 0:
        if 0 <= n <= 2:
            return n
        if n is 3:
            return 4
        l = [None] * n
        l[0] = 0
        l[1] = 1
        l[2] = 2
        l[3] = 4
        i = 4
        while i < n:
            l[i] = l[i - 1] + l[i - 2] + l[i - 3]
            i += 1
        return l[n - 1] + l[n - 2] + l[n - 3]


# Bottom Up Dynamic Programming/Tabulation (no list) Approach: O(n) runtime, O(1) space.
def tabulation_triple_step(n):
    if n is not None and n >= 0:
        if 0 <= n <= 2:
            return n
        if n == 3:
            return 4
        a = 1
        b = 2
        c = 4
        i = 4
        while i < n:
            temp = c + b + a
            a = b
            b = c
            c = temp
            i += 1
        return a + b + c


for i in range(10):
    print(f"rec_triple_step({i}):", rec_triple_step(i))
print()

for i in range(10):
    print(f"top_down_triple_step({i}):", top_down_triple_step(i))
print()

for i in range(10):
    print(f"tabulation_with_list_triple_step({i}):", tabulation_with_list_triple_step(i))
print()

for i in range(10):
    print(f"tabulation_triple_step({i}):", tabulation_triple_step(i))


