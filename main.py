def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("—" * 9)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("—" * 9)
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_win(board):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
                        (0, 4, 8), (2, 4, 6)]  # diagonal
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True
    return False

def check_tie(board):
    return " " not in board

def get_move(player, board):
    while True:
        move = input(f"{player}, enter a number (1-9) to make a move: ")
        if move.isdigit() and int(move) in range(1, 10) and board[int(move) - 1] == " ":
            return int(move) - 1
        print("Invalid move. Try again.")

def play():
    board = [" "] * 9
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        move = get_move(players[turn], board)
        board[move] = players[turn]
        if check_win(board):
            print_board(board)
            print(f"{players[turn]} wins!")
            break
        if check_tie(board):
            print_board(board)
            print("Tie!")
            break
        turn = (turn + 1) % 2

play()
