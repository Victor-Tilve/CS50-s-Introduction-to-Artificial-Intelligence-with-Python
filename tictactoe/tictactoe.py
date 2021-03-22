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
## NOTE: this function is done
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_turn = player(board)
    row, column = action
    board[row][column] = player_turn
    return board
## FIXME: would be interting to implement the stack iteration
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Check mean diagonal
    if board[0][0] != None:
        if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            # print("Checking diagonal 2")
            return board[0][0]
    #Check second diagonal
    if board[0][2] != None:
        if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
            # print("Checking diagonal 2")
            return board[0][2]

    #Check horizontal
    if board[0][0] != None:
        if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
            print(board[0][0])
            print(board[0][1])
            print(board[0][2])
            # print("Checking horizontal 1")
            return board[0][0]
    if board[1][0] != None:
        if board[1][0] == board[1][1] and board[1][0] == board[1][2]:
            # print("Checking horizontal 2")
            return board[1][0]
    if board[2][0] != None:
        if board[2][0] == board[2][1] and board[2][0] == board[2][2]:
            # print("Checking horizontal 3")
            return board[2][0]
    #Check Vertical
    if board[0][0] != None:
        if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
            # print("Checking Vertical 1")
            return board[0][0]
    if board[0][1] != None:
        if board[0][1] == board[1][1] and board[0][1] == board[2][1]:
            # print("Checking Vertical 2")
            return board[0][1]
    if board[0][2] != None:
        if board[0][2] == board[1][2] and board[0][2] == board[2][2]:
            # print("Checking Vertical 3")
            return board[0][2]

    return None
## FIXME: check is there is a better way
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        for row in range(len(board)):
            if None in board[row]:
                return False
    else:
        return True
    # raise NotImplementedError

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            max_value()
    # raise NotImplementedError

## COMBAK: CHeck how to implement these functions
def max_value(board):
    if terminal(board):
        return utility(board)
    v = (float(-inf),float(-inf))
    o_action = None
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float(inf)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
