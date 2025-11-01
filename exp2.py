def print_board(board):
    for row in board:
        print(" ".join("Q" if i == row else "." for i in range(8)))
    print()

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_queens(board, col):
    if col == 8:
        print_board(board)
        return True
    for row in range(8):
        if is_safe(board, row, col):
            board[col] = row
            if solve_queens(board, col + 1):
                return True
    return False

board = [-1] * 8
solve_queens(board, 0)
