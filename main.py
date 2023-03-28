import random

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

def opposite_corner(corner):
    if corner == 0:
        opp = 8
    if corner == 2:
        opp = 6
    if corner == 6:
        opp = 2
    if corner == 8:
        opp = 0
    return opp

def win_or_block(board,bot,opp,move,available_moves):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
                        (0, 4, 8), (2, 4, 6)]  # diagonal
    # Bot Wins
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == bot and board[combo[2]] == ' ':
            move = combo[2]
            if move in available_moves:
                break
        if board[combo[0]] == board[combo[2]] == bot and board[combo[1]] == ' ':
            move = combo[1]
            if move in available_moves:
                break
        if board[combo[1]] == board[combo[2]] == bot and board[combo[0]] == ' ':
            move = combo[0]
            if move in available_moves:
                break
    # Bot Blocks
    if move == -1:
        for combo in win_combinations:
            if board[combo[0]] == board[combo[1]] == opp and board[combo[2]] == ' ':
                move = combo[2]
                if move in available_moves:
                    break
            if board[combo[0]] == board[combo[2]] == opp and board[combo[1]] == ' ':
                move = combo[1]
                if move in available_moves:
                    break
            if board[combo[1]] == board[combo[2]] == opp and board[combo[0]] == ' ':
                move = combo[0]
                if move in available_moves:
                    break
    return move

def bot_move(bot, board, bot_turn):
    move = -1
    corners = [0,2,6,8]
    edges = [1,3,5,7]
    if bot == 'X':
        opp = 'O'
    else:
        opp = 'X'

    opp_moves = [i for i in range(9) if board[i] == opp]
    bot_moves = [i for i in range(9) if board[i] == bot]
    available_moves = [i for i in range(9) if board[i] == " "]

    if bot_turn == 1:
        if opp == 'X':
            if 4 not in opp_moves:
                move = 4
            else:
                move = random.choice(corners)
        else:
            move = random.choice(corners)
    else:
        if bot_turn == 2:
            if opp == 'O':
                if opp_moves[0] in edges or opp_moves[0] == opposite_corner(bot_moves[0]):
                    move = 4
                else:
                    move = opposite_corner(bot_moves[0])
            else:
                if opp == 'X':
                    edge1 = [0,1,5,8]
                    edge2 = [2,5,7,6]
                    edge3 = [8,7,3,0]
                    edge4 = [6,3,1,2]
                    if opp_moves[0] in edge1 and opp_moves[1] in edge1:
                        if opp_moves[0] == 0 or opp_moves[1] == 0:
                            move = 8
                        else:
                            move = 0
                    if opp_moves[0] in edge2 and opp_moves[1] in edge2:
                        if opp_moves[0] == 2 or opp_moves[1] == 2:
                            move = 6
                        else:
                            move = 2
                    if opp_moves[0] in edge3 and opp_moves[1] in edge3:
                        if opp_moves[0] == 0 or opp_moves[1] == 0:
                            move = 8
                        else:
                            move = 0
                    if opp_moves[0] in edge4 and opp_moves[1] in edge4:
                        if opp_moves[0] == 2 or opp_moves[1] == 2:
                            move = 6
                        else:
                            move = 2
                    if opp_moves[0] in corners and opp_moves[1] in corners:
                        for edge in edges:
                            if edge in available_moves:
                                edges.remove(edge)
                        move = random.choice(edges)
                    else:
                        move = win_or_block(board, bot, opp, move, available_moves)
        else:
            move = win_or_block(board, bot, opp, move, available_moves)

    if move == -1:
        for corner in corners:
            if corner not in available_moves:
                corners.remove(corner)
        if len(corners) != 0:
            move = random.choice(corners)
        else:
            if 7 in available_moves:
                move = 7
            else:
                move = random.choice(available_moves)
    print(f'Bot filled {bot} in slot {move + 1}!')
    return move

def play():
    board = [" "] * 9
    players = ["X", "O"]
    turn = 0
    bot_turn = 1

    while True:
        mode = input('Game Mode: Single Player or Multiplayer (s/m)? ')
        if mode == 's' or mode == 'm':
            if mode == 's':
                while True:
                    select = input('Player Selection: X or O (x/o)? ')
                    if select == 'x':
                        player_turn = 0
                        break
                    else:
                        if select == 'o':
                            player_turn = 1
                            break
                        print('Not a valid Player. Try again.')
            break
        else:
            print('Not a valid Game Mode. Try again.')
    while True:
        print_board(board)
        if mode == 's':
            if turn == player_turn:
                move = get_move(players[turn], board)
            else:
                move = bot_move(players[turn], board, bot_turn)
                bot_turn += 1
        else:
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
