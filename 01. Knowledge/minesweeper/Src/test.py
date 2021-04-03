from minesweeper import *

# board = Minesweeper()
# board.print()
test = []
height = 2
width = 2
cell = (0,1)
row, column = cell
neighbors = set()
for i in range(row - 1, row + 2, 1):
    for j in range(column - 1, column + 2, 1):
        if i >= 0 and i <= height:
            if j >= 0 and j <= width:
                if (row,column) != (i,j) and (i,j) not in test:
                    neighbors.add((i,j))
print(f'{neighbors}')
