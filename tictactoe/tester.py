import tictactoe as ttt

EMPTY = None

board = ttt.initial_state()

board = [["O", "X", "X"],
        ["O", "X", EMPTY],
        [EMPTY, "X", EMPTY]]


# board = ttt.result(board, (2,2))
print(board)


def main():
     n = 9001
     print(f"Initial address of n: {id(n)}")
     increment(n)
     print(f"  Final address of n: {id(n)}")
     print(f"  Final value of n: {n}")

def increment(x):
    print(f"Initial address of x: {id(x)}")
    x += 1
    print(f"  Final address of x: {id(x)}")

x = 2
print(ttt.utility(board))
