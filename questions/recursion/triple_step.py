"""
    TRIPLE STEP (CCI 8.1)

    A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
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
def triple_step_rec(n):

    def _triple_step_rec(n):
        if n is 0 or n is 1 or n is 2:
            return n
        if n is 3:
            return 4
        return _triple_step_rec(n - 1) + _triple_step_rec(n - 2) + _triple_step_rec(n - 3)

    if n is not None and n >= 0:
        return _triple_step_rec(n)


# Top Down Dynamic Programming/Memoization Approach: O(n) runtime, O(n) space.
def triple_step_top_down(n):

    def _triple_step_top_down(n, memo):
        if n is 0 or n is 1 or n is 2:
            return n
        if n is 3:
            return 4
        if memo[n] is None:
            memo[n] = _triple_step_top_down(n - 1, memo) + _triple_step_top_down(n - 2, memo) + _triple_step_top_down(n - 3, memo)
        return memo[n]

    if n is not None and n >= 0:
        memo = [None] * (n + 1)
        return _triple_step_top_down(n, memo)


# Bottom Up Dynamic Programming/Tabulation with a list Approach: O(n) runtime, O(n) space.
def triple_step_bottom_up_memo(n):
    if n is not None and n >= 0:
        if n is 0 or n is 1 or n is 2:
            return n
        if n is 3:
            return 4
        memo = [None] * n
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2
        memo[3] = 4
        i = 4
        while i < n:
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
            i += 1
        return memo[n - 1] + memo[n - 2] + memo[n - 3]


# Bottom Up Dynamic Programming/Tabulation (no list) Approach: O(n) runtime, O(1) space.
def triple_step_bottom_up(n):
    if n is not None and n >= 0:
        if n is 0 or n is 1 or n is 2:
            return n
        if n is 3:
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


# Variation: How to climb up n steps, any number at a time.
def n_steps_rec(n):
    def _n_steps_rec(n):
        if n is 0:
            return 0
        sum = 0
        for i in range(n):
            sum += _n_steps_rec(i)
        return sum + 1

    if n is not None and n >= 0:
        return _n_steps_rec(n)


def n_steps_top_down(n):
    def _n_steps_top_down(n, memo):
        if n is 0 or n is 1:
            return n
        if memo[n] is None:
            memo[n] = 1
            for i in range(n):
                memo[n] += _n_steps_top_down(i, memo)
        return memo[n]

    if n is not None and n >= 0:
        memo = [None for _ in range(n + 1)]
        return _n_steps_top_down(n, memo)


def n_steps_bottom_up(n):
    if n is not None and n >= 0:
        if n is 0 or n is 1:
            return n
        memo = [None for _ in range(n + 1)]
        memo[0] = 0
        memo[1] = 1
        for i in range(2, n + 1):
            memo[i] = 1
            for j in range(0, i):
                memo[i] += memo[j]
        return memo[n]


# Variation: How to climb up n steps either 1, 3, or 5 steps at a time.
def one_three_five_steps_rec(n):
    def _one_three_five_steps_rec(n):
        if n is 0 or n is 1 or n is 5:
            return n
        if n is 2 or n is 3 or n is 4:
            return n - 1
        return _one_three_five_steps_rec(n - 1) + _one_three_five_steps_rec(n - 3) + _one_three_five_steps_rec(n - 5)

    if n is not None and n >= 0:
        return _one_three_five_steps_rec(n)


def one_three_five_steps_top_down(n):
    def _one_three_five_steps_top_down(n, memo):
        if n is 0 or n is 1 or n is 5:
            return n
        if n is 2 or n is 3 or n is 4:
            return n - 1
        if memo[n] is None:
            memo[n] = _one_three_five_steps_top_down(n - 1, memo) + _one_three_five_steps_top_down(n - 3, memo) + _one_three_five_steps_top_down(n - 5, memo)
        return memo[n]

    if n is not None and n >= 0:
        memo = [None for _ in range(n + 1)]
        return _one_three_five_steps_top_down(n, memo)


def one_three_five_steps_bottom_up(n):
    if n is not None and n >= 0:
        if n is 0 or n is 1 or n is 5:
            return n
        if n is 2 or n is 3 or n is 4:
            return n - 1
        memo = [None for _ in range(n + 1)]
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        memo[3] = 2
        memo[4] = 3
        memo[5] = 5
        i = 6
        while i < n:
            memo[i] = memo[i - 1] + memo[i - 3] + memo[i - 5]
            i += 1
        return memo[i - 1] + memo[i - 3] + memo[i - 5]


n = 12
for i in range(n):
    print(f"triple_step_rec({i}): {triple_step_rec(i)}")
print()

for i in range(n):
    print(f"triple_step_top_down({i}): {triple_step_top_down(i)}")
print()

for i in range(n):
    print(f"triple_step_bottom_up_memo({i}): {triple_step_bottom_up_memo(i)}")
print()

for i in range(n):
    print(f"triple_step_bottom_up({i}): {triple_step_bottom_up(i)}")
print()

for i in range(n):
    print(f"n_steps_rec({i}): {n_steps_rec(i)}")
print()

for i in range(n):
    print(f"n_steps_top_down({i}): {n_steps_top_down(i)}")
print()

for i in range(n):
    print(f"n_steps_bottom_up({i}): {n_steps_bottom_up(i)}")
print()

for i in range(n):
    print(f"one_three_five_steps_rec({i}): {one_three_five_steps_rec(i)}")
print()

for i in range(n):
    print(f"one_three_five_steps_top_down({i}): {one_three_five_steps_top_down(i)}")
print()

for i in range(n):
    print(f"one_three_five_steps_bottom_up({i}): {one_three_five_steps_bottom_up(i)}")
print()


