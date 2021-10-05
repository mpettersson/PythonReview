"""
    MATRIX CHAIN MULTIPLICATION

    Write a function, which when given an integer list representing matrices, computes the optimal ORDER, or the order
    with the MINIMUM number of operations to multiply the matrices.  The list (l), of length n, represents n-1 matrices,
    where matrix[i] has the dimensions l[i-1] rows by l[i] columns.

    NOTE: Don't compute the result, find the fastest way to compute the result. Computing the optimal order first then
          multiplying will take less time than no ordering and an inefficient multiplication.

    REMEMBER: Matrix multiplication is associative: A(BC) = (AB)C.

    For example, imagine that you were tasked with computing the multiplication of six matrices (A1 - A6), where the
    matrices have the following dimensions:
            A1 = 30 x 35
            A2 = 35 x 15
            A3 = 15 x 5
            A4 = 5 x 10
            A5 = 10 x 20
            A6 = 20 x 25
    In what order would you multiply them to MINIMIZE the number of operations?

    Example:
        Input = [30, 35, 15, 5, 10, 20, 25]
        Output =

    Matrix Notes:
        - To be able to multiply two matrices, A and B, the number of A's columns must EQUAL the number of B's rows.
        - Each cell in C will take q multiplications (where q is the num of A's cols and B's rows).
        - Num of C's rows = Num of A's rows.
        - Num of C's cols = Num of B's cols.
        - Total cells in C = len(A) * len(B[0])
        - Matrix multiplication is associative: A(BC) = (AB)C.
        - The time required for A x B x C could be affected by which two matrices are multiplied first.

    Matrix Multiplication Examples:

                  (4 x 2)                    (2 x 3)                           (4 x 3)
            A = [[a00, a01],        B = [[b00, b01, b02],       AxB = C = [[c00, c01, c02],
                 [a10, a11],             [b10, b11, b12]]                  [c10, c11, c12],
                 [a20, a21],                                               [c20, c21, c22],
                 [a30, a31]]                                               [c30, c31, c32]]

            c00 = (a00 * b00) + (a01 * b10)
            c01 = (a00 * b01) + (a01 * b11)
                         ...
            c31 = (a30 * b01) + (a31 * b11)
            c32 = (a30 * b02) + (a31 * b12)

        With generalized sizes:

            A = [[a00, a01, ..., a0n],        B = [[b00, b01, ..., b0p],    AxB = C = [[c00, c01, ..., c02],
                 [a10, a11, ..., a1n],             [b10, b11, ..., b1p],               [c10, c11, ..., c12],
                         ...                               ...                                  ...
                 [am0, am1, ..., amn]]             [bn0, bn1, ..., bnp]]               [c30, c31, ..., c32]]

            cij = (ai0 * b0j) + (ai1 * b1j) + ... + (ain * bnj) = Sum of (aik * bkj) for k in range 1 through n.

        With n matrices in the multiplication chain there are n-1 binary operations and Cn-1 ways of placing
        parentheses, where Cn-1 is the (n-1)th Catalan number.  The formula to find the nth Catalan number is:
                  (2n)!
                --------   or   (math.factorial(2 * n)) / (math.factorial(n + 1) * math.factorial(n))
                (n+1)!n!

    Variations:
        - find_max_score_popped_balloons.py (leetcode.com/problems/burst-balloons/)
        - Minimum weight convex polygon triangulation (just has a different cost function).
        - Concatenating singly linked lists.

    References:
        - youtube.com/watch?v=JMql7zF87aE
        - techiedelight.com/matrix-chain-multiplication
        - medium.com/@avik.das/dynamic-programming-deep-dive-chain-matrix-multiplication-a3b8e207b201
"""


# Questions you should ask the interviewer (if not explicitly stated):
#   - What time/space complexity are you looking for?
#   - Ask clarification questions about the INPUT LIST (this is very easy to misunderstand on the first encounter).
#   - Ask clarification questions about matrix multiplication.


# APPROACH: Plain/Naive Recursion W/O Parenthesizations
#
# For ALL possible ways to multiply the matrices, i.e., all PARENTHESIZATIONS not permutations, find the OPTIMAL number
# of operations.  This approach produces only the optimal cost, not the actual parenthesizations.  For both the cost and
# parenthesizations, see the next approach.
#
# Time Complexity: O(2 ** n), where n is the number of matrices to be multiplied.
# Space Complexity: Depends on implementation.
#
# NOTE: The number of ways (and time complexity) ends up being the Catalan numbers, or O((4 ** n) / (n ** (3 / 2))).
def matrix_chain_multiplication_cost_only_rec(l):

    def _rec(dims, i, j):
        if i == j:                                          # Base Case: A single matrix.
            return 0
        min_cost = float('inf')                             # The minimum cost result to be returned.
        for k in range(i, j):                               # Where the (parenthesis) split is made.
            cost = _rec(dims, i, k)                         # recur for M[i+1] ... M[k] to get an i x k matrix
            cost += _rec(dims, k+1, j)                      # recur for M[k+1] ... M[j] to get an k x j matrix
            cost += dims[i-1] * dims[k] * dims[j]           # cost to multiply two i x k and k x j matrix
            if cost < min_cost:
                min_cost = cost
        return min_cost                                     # Minimum cost to multiply M[j+1] ... M[j]

    if isinstance(l, list):
        return _rec(l, 1, len(l)-1)                         # NOTE: BE CAREFUL OF INITIAL VALUES!


# APPROACH: Plain/Naive Recursion
#
# In addition to the minimum cost needed to multiply the supplied matrices, this approach also returns the
# parenthesizations of the supplied matrices.
#
# Time Complexity: O(2 ** n), where n is the number of matrices to be multiplied.  (Catalan Numbers)
# Space Complexity: Depends on implementation.
def matrix_chain_multiplication_rec(l):

    def _rec(dims, i, j):
        if i == j:                                          # Base Case: A single matrix.
            return 0, f"{dims[i-1]}x{dims[i]}"
        result = float('inf'), ""                           # Minimum Cost, and parenthesization to get it.
        for k in range(i, j):                               # Where the (parenthesis) split is made.
            left = _rec(dims, i, k)                         # Find optimal cost/parenthesization solution for the left.
            right = _rec(dims, k+1, j)                      # Find optimal cost/parenthesization solution for the right.
            cost = left[0] + right[0] + dims[i-1] * dims[k] * dims[j]     # Calculate current solution cost.
            if cost < result[0]:                            # Update result, if needed.
                result = cost, f"({left[1]} * {right[1]})"
        return result                                       # Return minimum Cost, and corresponding parenthesization.

    if isinstance(l, list):
        return _rec(l, 1, len(l)-1)


# APPROACH: Plain/Naive Recursion With MxCost Object
#
# This approach uses the MxCost Class (see below) to abstract away the math.  Although a list of MxCost objects is first
# created, the algorithms logic is identical to the approaches above, just presented and organized better.
#
# Time Complexity: O(2 ** n), where n is the number of matrices to be multiplied.  (Catalan Numbers)
# Space Complexity: Depends on implementation.
def matrix_chain_multiplication_rec_via_mxcost(l):

    def _rec(dims, i, j):
        if i == j:                                            # Base Case: A single matrix.
            return dims[i]
        result = None                                           # MxCost object with min cost.
        for k in range(i, j):
            left = _rec(dims, i, k)
            right = _rec(dims, k+1, j)
            candidate = left.multiply(right)
            if result is None or result.cost > candidate.cost:
                result = candidate
        return result                                          # MxCost object with min cost.

    if isinstance(l, list):
        mx_list = [MxCost(l[i-1], l[i]) for i in range(1, len(l))]
        result = _rec(mx_list, 0, len(mx_list)-1)
        return (result.cost, result.parenthesization()) if isinstance(result, MxCost) else None


# APPROACH: Top Down Dynamic Programming W/ Memoization
#
# This approach is essentially an optimized version of the plain recursion approach above; it calculates the cost of
# each possible parenthesization.  The optimization is simply to save the results of computations, thus eliminating
# redundant calculations.
#
# Time Complexity: O(n ** 3), where n is the total number of matrices.
# Space Complexity: O(n ** 2), where n is the total number of matrices.
def matrix_chain_multiplication_memo(l):

    def _parenthesize_result(l, b, i, j):                   # Helper fn to build parenthesized string representation.
        if i == j:
            return f"{l[i-1]}x{l[i]}"
        else:
            return f"({_parenthesize_result(l, b, i, b[i][j])} * {_parenthesize_result(l, b, b[i][j]+1, j)})"

    def _rec(dims, i, j, memo):
        if i == j:                                          # Single matrix, base case.
            return 0
        if memo[i][j] is None:
            memo[i][j] = float('inf')
            for k in range(i, j):                           # Split point.
                left = _rec(dims, i, k, memo)
                right = _rec(dims, k+1, j, memo)
                cost = left + right + dims[i-1] * dims[k] * dims[j]
                if cost < memo[i][j]:
                    memo[i][j] = cost
                    back[i][j] = k
        return memo[i][j]

    if isinstance(l, list):
        n = len(l)
        memo = [[None] * n for _ in range(n)]               # NOTE: 1 extra row & column for simplified implementation.
        back = [[0] * n for _ in range(n)]                  # NOTE: 1 extra row & column for simplified implementation.
        result = _rec(l, 1, n-1, memo), _parenthesize_result(l, back, 1, n-1)
        # print("memo:\n", format_matrix(memo), "\nback:\n", format_matrix(back))
        return result


# APPROACH: Top Down Dynamic Programming W/ Memoization With MxCost Object
#
# This approach uses the MxCost Class (see below) to abstract away the math.  Although a list of MxCost objects is first
# created, the remaining logic is identical to the top down dynamic programming, or the cached recursive approach above.
#
# Time Complexity: O(n ** 3), where n is the total number of matrices.
# Space Complexity: O(n ** 2), where n is the total number of matrices.
def matrix_chain_multiplication_memo_via_mxcost(l):

    def _rec(dims, i, j, memo):
        if i == j:                                          # A single matrix, base case.
            return dims[i]
        if memo[i][j] is None:
            for k in range(i, j):
                left = _rec(dims, i, k, memo)
                right = _rec(dims, k+1, j, memo)
                candidate = left.multiply(right)
                if memo[i][j] is None or memo[i][j].cost > candidate.cost:
                    memo[i][j] = candidate
        return memo[i][j]                                   # Returns a MxCost object with min cost.

    if isinstance(l, list):
        mx_list = [MxCost(l[i-1], l[i]) for i in range(1, len(l))]
        n = len(mx_list)
        if n > 1:
            memo = [[None] * n for _ in range(n)]
            _rec(mx_list, 0, n-1, memo)
            return memo[0][-1].cost, memo[0][n-1].parenthesization()
        return mx_list[0].cost, mx_list[0].parenthesization()


# APPROACH: Tabulation/Bottom Up Dynamic Programming W/ Memoization
#
# This approach builds a memoization table of matrix multiplication costs, starting with matrix chains of length two
# (since single matrices have a default cost of 0).  A similar sized table is maintained to be able to "backtrack" the
# process and build the parenthesization for the optimal matrix multiplications.  To minimize any additional confusion
# and "off by one errors", both the memo and backtrack tables are padded with additional rows/columns to allow for
# 1-based indexing (as opposed to 0-based).  The following two tables are the memoization and backtracking tables for
# the example in the description:
#
#           0     0     0     0     0     0     0               0 0 0 0 0 0 0
#           0     0     15750 7875  9375  11875 15125           0 0 1 1 3 3 3
# 	        0     0     0     2625  4375  7125  10500           0 0 0 2 3 3 3
# 	        0     0     0     0     750   2500  5375            0 0 0 0 3 3 3
# 	        0     0     0     0     0     1000  3500            0 0 0 0 0 4 5
# 	        0     0     0     0     0     0     5000            0 0 0 0 0 0 5
#           0     0     0     0     0     0     0               0 0 0 0 0 0 0
#
#  For example, the value (7125) for memo[2][5] above was the minimum value of:
#       memo[2][2] + memo[3][5] + l1 * l2 * l5  = 0 + 2500 + 35 * 15 * 20   = 13000
#       memo[2][3] + memo[4][5] + l1 * l3 * l5  = 2625 + 1000 + 35 * 5 * 20 = 7125
#       memo[2][4] + memo[5][5] + l1 * l4 * l5  = 4375 + 0 + 35 * 10 * 20   = 11375
#  Once a minimum is found the corresponding split location (3) is recorded in the backtrack table (back[2][5]).
#
# Time Complexity: O(n ** 3), where n is the total number of matrices.
# Space Complexity: O(n ** 2), where n is the total number of matrices.
def matrix_chain_multiplication_tab(l):

    def _parenthesize_result(l, b, i, j):                   # Helper fn to build parenthesized string representation.
        if i == j:                                          # Base case: The dimensions of a matrix.
            return f"{l[i-1]}x{l[i]}"
        else:                                               # Recursive case: Groups parenthesis by saved split points.
            return f"({_parenthesize_result(l, b, i, b[i][j])} * {_parenthesize_result(l, b, b[i][j]+1, j)})"

    if isinstance(l, list):
        n = len(l)
        memo = [[0] * n for _ in range(n)]                  # NOTE: 1 extra row & column for simplified implementation.
        back = [[0] * n for _ in range(n)]                  # NOTE: 1 extra row & column for simplified implementation.
        for length in range(2, n):                          # The number of matrices being multiplied (chain length).
            for i in range(1, n - length + 1):              # i is the (chain's) starting index.
                j = i + length - 1                          # j is the (chain's) ending index.
                memo[i][j] = float('inf')
                for k in range(i, j):                       # k is the split point (the parens go between k and k+1).
                    cost = memo[i][k] + memo[k+1][j] + l[i-1] * l[k] * l[j]
                    if cost < memo[i][j]:
                        memo[i][j] = cost
                        back[i][j] = k                      # Update the backtracking info for parenthesization.
        # print("memo:\n", format_matrix(memo), "\nback:\n", format_matrix(back))
        return memo[1][-1], _parenthesize_result(l, back, 1, n-1)


# APPROACH: MxCost Object Tabulation/Bottom Up Dynamic Programming W/ Memoization
#
# This approach uses the MxCost object to abstract away implementation/math details, thus providing a cleaner, more
# readable solution.  A memoization table is still used, this time it contains pointers to the MxCost objects as opposed
# to actual costs, however, the backtracking table is no longer needed.  This is due to the inclusion of the backtrack
# info in the MxCost class' left and right MxCost pointers.  The left and right pointer are only populated when a
# matrix is formed from the multiplication of two other matrices.
#
# Time Complexity: O(n ** 3), where n is the total number of matrices.
# Space Complexity: O(n ** 2), where n is the total number of matrices.
def matrix_chain_multiplication_tab_via_mxcost(l):
    if isinstance(l, list):
        mx_list = [MxCost(l[i-1], l[i]) for i in range(1, len(l))]
        n = len(mx_list)
        memo = [[None] * n for _ in range(n)]

        for i in range(n):                          # Assign the "bottom of the triangle"
            memo[i][i] = mx_list[i]

        for sub_seq_len in range(1, n):
            for i in range(n - sub_seq_len):
                k = i
                j = i + sub_seq_len
                while k < j:
                    candidate = memo[i][k].multiply(memo[k+1][j])
                    if memo[i][j] is None or candidate.cost < memo[i][j].cost:
                        memo[i][j] = candidate
                    k += 1

        return (memo[0][-1].cost, memo[0][-1].parenthesization()) if isinstance(memo[0][-1], MxCost) else None


# (Helper) MxCost Class
#
# This class simplifies the logic by abstracting away much of the math; it makes understanding the process much easier
# and is worth the extra effort!
#
# For example, given the following matrices:
#       a = MxCost(2, 3)
#       b = MxCost(3, 7)
#       c = MxCost(7, 10)
#
# If multiplying two matrices (a and b), the resulting matrix is produced (with proper dimensions and cost):
#       ab = a.multiply(b)
#       print(ab.rows, ab.cols, ab.cost)      # would print: 2 7 42 or, 2 rows, 7 columns, and ab has a cost of 42.
#
# Furthermore, the parenthesization of resultant matrices can easily be shown:
#       print(ab.parenthesization())    # would print: (2x3 * 3x7)
class MxCost:
    def __init__(self, rows, cols, cost=0, left=None, right=None):
        self.rows = rows                # Number of rows.
        self.cols = cols                # Number of columns.
        self.cost = cost                # Cost to get here (if this matrix was the product of other matrices).
        self.left = left                # This is needed to build the parenthesization.
        self.right = right              # This is needed to build the parenthesization.

    def cost_fn(self, m):               # Cost function when multiplying two matrices.
        return self.rows * self.cols * m.cols + self.cost + m.cost

    def multiply(self, m):              # Returns a new matrix, of proper dimensions, and associated cost.
        return MxCost(self.rows, m.cols, self.cost_fn(m), self, m)

    def parenthesization(self):         # This returns a string representing how this matrix was formed.
        if self.left is None:
            return f"{self.rows}x{self.cols}"
        return f"({self.left.parenthesization()} * {self.right.parenthesization()})"


def format_matrix(m):
    try:
        w = max([len(str(e)) for r in m for e in r]) + 1
    except (ValueError, TypeError):
        return f"\n{None}"
    return m if not m else '\t' + '\n\t'.join([''.join([f'{e!r:{w}}' for e in r if len(r) > 0]) for r in m if len(m) > 0])


# NOTE: Each of the following lists represents a series of matrices to be multiplies, where for an index i in the list,
#       the matrix M[i] has the dimensions list[i-1] (number of rows) x list[i] (number of columns).
lists = [[10, 30, 5, 60],                           # 4500,  ((10x30 * 30x5) * 5x60)
         [30, 35, 15, 5, 10],                       # 9375,  ((30x35 * (35x15 * 15x5)) * 5x10)
         [2, 3, 7, 10],                             # 182,   ((2x3 * 3x7) * 7x10)
         [30, 35, 15, 5, 10, 20, 25],               # 15125, ((30x35 * (35x15 * 15x5)) * ((5x10 * 10x20) * 20x25))
         [10, 30, 5],                               # 1500,  (10x30 * 30x5)
         [10, 30],                                  # 0,     10x30
         None]
fns = [matrix_chain_multiplication_cost_only_rec,
       matrix_chain_multiplication_rec,
       matrix_chain_multiplication_rec_via_mxcost,
       matrix_chain_multiplication_memo,
       matrix_chain_multiplication_memo_via_mxcost,
       matrix_chain_multiplication_tab,
       matrix_chain_multiplication_tab_via_mxcost]

for l in lists:
    print(f"l: {l}")
    for fn in fns:
        print(f"{fn.__name__}(l): {fn(l)}")
    print()


