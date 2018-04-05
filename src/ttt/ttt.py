# Tic tac toe game

import os
from math import floor

# Consts
board_columns = 3
board_rows = 3

def display_board(board):
    # Clear the current output
    #os.system('cls')
    
    for row in range(board_rows):
        print('')
        for column in range(board_columns):
            print(board[row][column], end='')
    print('')

def make_move(player_symbol, move, board):
    (i, j) = get_cell_from_position(move)
    board[i][j] = player_symbol

def get_cell_from_position(pos):
    pos -= 1
    row = board_columns -1 - floor(pos / board_columns)
    col = pos % 3
    print(row)
    print(col)
    return (row, col)

def game_completed(board):
    pass

def start_game():
    print('starting game!')

    p1_sym = input('Player one choose a symbol: ')
    p2_sym = input('Player two choose a symbol: ')

    board = [[0 for x in range(board_columns)] for y in range(board_rows)]
    current_player = 1

    while not game_completed(board):
        display_board(board)

        move = int(input(f'Player {current_player} make a move:' ))

        make_move(p1_sym if current_player == 1 else p2_sym, move, board)

        current_player = 2 if current_player == 1 else 1

start_game()