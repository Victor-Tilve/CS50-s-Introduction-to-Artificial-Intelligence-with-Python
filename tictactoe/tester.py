import tictactoe as ttt
import sys
EMPTY = None
sys.setrecursionlimit(1000000)
# board = ttt.initial_state()

'''board = [["O", "X", EMPTY],
        ["O", "X", EMPTY],
        ["X","O", EMPTY]]'''

board = [[EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]
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

# x = ttt.max_value(board)
# print(ttt.winner(board))
# print(ttt.terminal(board))
# print(board[0][0])
# print(ttt.player(board))
# limit = sys.getrecursionlimit()
# print(ttt.player(board))
print(ttt.minimax(board))
