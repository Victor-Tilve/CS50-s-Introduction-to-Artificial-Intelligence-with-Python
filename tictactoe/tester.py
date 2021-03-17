import tictactoe as ttt

EMPTY = None

board = ttt.initial_state()

board = [[EMPTY, "X", EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]


board = ttt.result(board, (0,0))
# print(board)


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
print(id(x))

x = 5
print(id(x))
