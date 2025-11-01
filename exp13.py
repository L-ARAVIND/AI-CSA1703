# Q13: Minimax Algorithm for Tic Tac Toe

import math

def print_board(board):
    for i in range(3):
        print(board[i])
    print()

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != '_':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '_':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '_':
        return board[0][2]
    return None

def minimax(board, depth, isMax):
    winner = check_winner(board)
    if winner == 'O': return 1
    if winner == 'X': return -1
    if all(cell != '_' for row in board for cell in row): return 0

    if isMax:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    best = max(best, minimax(board, depth+1, False))
                    board[i][j] = '_'
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    best = min(best, minimax(board, depth+1, True))
                    board[i][j] = '_'
        return best

board = [['_','_','_'],['_','_','_'],['_','_','_']]
print("Initial empty board:")
print_board(board)
print("Score (AI assuming O):", minimax(board, 0, True))
