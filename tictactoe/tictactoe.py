"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

## NOTE: this function is done
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_counter = 0
    o_counter = 0

    for row in range(3):
        for column in range(3):
            if board[row][column] == "X":
                x_counter += 1
            elif board[row][column] == "O":
                o_counter += 1
    # print(f"x_counter: {x_counter}")
    # print(f"o_counter: {o_counter}")
    if x_counter == 0:
        return X

    if x_counter > o_counter:
        return O

    elif x_counter == o_counter:
        return X

## NOTE: this function is done
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_states = set()

    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY:
                possible_states.add((row,column))
    return possible_states

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_turn = player(board)
    row, column = action
    board[row][column] = player_turn
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
