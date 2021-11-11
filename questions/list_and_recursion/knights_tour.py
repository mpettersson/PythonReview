"""
    KNIGHT'S TOUR

    A knight's tour is a sequence of moves of a knight on a chessboard such that the knight visits every square exactly
    once.  If the knight ends on a square that is one (knight's) move from the beginning square (so that it could tour
    the board again immediately, following the same path), the tour is closed; otherwise, it is open.

    Write an algorithm that takes an int representing the size of the board (n), and then returns a matrix representing
    the moves of a valid Knight's tour.

    Variations on this problem can include:
        - Irregular shaped boards.
        - A closed Knight's tour path.
        - Using prioritized moves (e.g., moves left before right, up before down, etc.).
"""


#  This function solves the Knight Tour problem via backtracking.
def knights_tour(n, start_row=0, start_col=0):

    def _is_valid_move(row, col, board):
        return True if 0 <= row < len(board) and 0 <= col < len(board) and board[row][col] == -1 else False

    def _knights_tour(board, curr_row, curr_col, knights_moves, count=1):
        if count == (len(board) * len(board[0])):
            return True
        for (delta_row, delta_col) in knights_moves:        # For each possible knight move.
            next_row = curr_row + delta_row
            next_col = curr_col + delta_col
            if _is_valid_move(next_row, next_col, board):   # Check if next move is on the board.
                board[next_row][next_col] = count
                if _knights_tour(board, next_row, next_col, knights_moves, count + 1):
                    return True
                board[next_row][next_col] = -1              # Backtracking
        return False

    board = [[-1 for i in range(n)] for i in range(n)]
    knights_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    board[start_row][start_col] = 0
    if _knights_tour(board, start_row, start_col, knights_moves):
        return board


def print_board(board):
    for row in range(len(board)):
        for col in range(len(board)):
            print(f"{board[row][col]:3}", end=' ')
        print()


import time
t = time.time()
print_board(knights_tour(6, 5, 5))
print("Took: ", time.time() - t)

# 8x8 Board Took: 54.49761986732483

