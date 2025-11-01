# Q12: Tic Tac Toe

board = [' ']*9

def print_board():
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def check_winner():
    combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in combos:
        if board[a]==board[b]==board[c] and board[a] != ' ':
            return True
    return False

turn = 'X'
for i in range(9):
    print_board()
    move = int(input(f"Player {turn}, enter position (0-8): "))
    if board[move]==' ':
        board[move] = turn
        if check_winner():
            print_board()
            print(f"Player {turn} wins!")
            break
        turn = 'O' if turn=='X' else 'X'
else:
    print("Draw!")
