"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

<<<<<<< HEAD
=======
max_Depth = 0
>>>>>>> Solution

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

<<<<<<< HEAD

=======
## NOTE: this function is done
>>>>>>> Solution
def player(board):
    """
    Returns player who has the next turn on a board.
    """
<<<<<<< HEAD
    raise NotImplementedError


=======
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
>>>>>>> Solution
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
<<<<<<< HEAD
    raise NotImplementedError


=======
    possible_states = set()

    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY:
                possible_states.add((row,column))
    return possible_states
## NOTE: this function is done
>>>>>>> Solution
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
<<<<<<< HEAD
    raise NotImplementedError


=======
    player_turn = player(board)
    row, column = action
    board[row][column] = player_turn
    return board
## FIXME: would be interting to implement the stack iteration
>>>>>>> Solution
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
<<<<<<< HEAD
    raise NotImplementedError


=======
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
            # print(board[0][0])
            # print(board[0][1])
            # print(board[0][2])
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
>>>>>>> Solution
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
<<<<<<< HEAD
    raise NotImplementedError

=======
    if winner(board) == None:
        for row in range(len(board)):
            if None in board[row]:
                return False
    else:
        return True
    # raise NotImplementedError
>>>>>>> Solution

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
<<<<<<< HEAD
    raise NotImplementedError
=======
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


    # raise NotImplementedError
>>>>>>> Solution


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
<<<<<<< HEAD
    """
    raise NotImplementedError
=======
    The move returned should be the optimal action (i, j) that is one of the allowable actions on the board.
    If multiple moves are equally optimal, any of those moves is acceptable.
    """
    ## COMBAK: imma bout to implemnt something i'm not source
    if terminal(board):
        return None
    else:
        # print("The game is not over")
        o_values = {}
        o_values[1] = []
        o_values[0] = []
        o_values[-1] = []

        if player(board) == X:
            # print(f"{X} Turn")
            for action in actions(board):
                value = max_value(result(board, action))
                if value == 1:
                    o_values[1].append(action)
                elif value == 0:
                    o_values[0].append(action)
                else:
                    o_values[-1].append(action)
            # print(o_values)
            if len(o_values[1]) > 0:
                    return o_values[1][0]
            elif len(o_values[0]) > 0:
                return o_values[0][0]
            else:
                return o_values[-1][0]

        elif player(board) == O:
            # print(f"{O} Turn")
            for action in actions(board):
                value = max_value(result(board, action))
                if value == 1:
                    o_values[1].append(action)
                elif value == 0:
                    o_values[0].append(action)
                else:
                    o_values[-1].append(action)
            # print(o_values)

            if len(o_values[-1]) > 0:
                    return o_values[-1][0]
            elif len(o_values[0]) > 0:
                return o_values[0][0]
            else:
                return o_values[1][0]

    # raise NotImplementedError

## COMBAK: CHeck how to implement these functions
def max_value(board):
    global max_Depth
    if terminal(board):
        return utility(board)
    if max_Depth > 8:
        return 1
    v = float('-inf')
    for action in actions(board):
        max_Depth += 1
        v = max(v, min_value(result(board, action)))
        if v == 1:
            return v
    return v


def min_value(board):
    global max_Depth

    if terminal(board):
        return utility(board)
    if max_Depth > 8:
        return -1
    v = float('inf')
    for action in actions(board):
        max_Depth += 1
        v = min(v, max_value(result(board, action)))
        if v == -1:
            return v
    return v
>>>>>>> Solution
