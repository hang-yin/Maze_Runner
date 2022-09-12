import numpy as np
import random
from state import find_all_neighbors

n = random.randint(4, 10)   # rows
m = random.randint(4, 10)   # cols
print('n: {}, m: {}'.format(n,m))

maze = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(1)
    maze.append(row)

def display_maze():
    for k in range(n):
        print(maze[k])
    print('\n')

display_maze()


# coordinates for building free cells
x = random.randint(0, n-1)
y = random.randint(0, m-1)

walls = []

# maze[x][y] = 0  # random cell to start creating free cells with (A)
neighbors = find_all_neighbors(maze, (x,y))     # returns a list of neighbor coords
for nbr in neighbors:
    walls.append(nbr)

wall_len = len(walls)
while len(walls) != 0:
    cell_C = walls[random.randint(0, wall_len-1)]   # C is a wall
    cell_A = (x, y)
    maze[cell_A[0]][cell_A[1]] = 0

    # check if C is an edge cell
    if cell_C[0] == 0 or cell_C[0] == n-1 or cell_C[1] == 0 or cell_C[1] == m-1:
        continue

    # A and C are in the same row
    if cell_A[0] == cell_C[0]:
        # C to the right of A
        if cell_C[1] > cell_A[1]:
            cell_B = (cell_A[0], cell_C[1]+1)
        
        # C to the left of A
        else:
            cell_B = (cell_A[0], cell_C[1]-1)

    # A and C are in the same column
    else:
        # C below A
        if cell_C[0] > cell_A[0]:
            cell_B = (cell_C[0]+1, cell_A[1])
        
        # C above A
        else:
            cell_B = (cell_C[0]-1, cell_A[1])

    # print(cell_A)
    # print(cell_B)
    if maze[cell_A[0]][cell_A[1]] == 1 or maze[cell_B[0]][cell_B[1]] == 1:
        if maze[cell_A[0]][cell_A[1]] == 1:
            cell_D = cell_A
        else:
            cell_D = cell_B

        maze[cell_C[0]][cell_C[1]] = 0
        maze[cell_D[0]][cell_D[1]] = 0

    walls.remove(cell_C)
    display_maze()

display_maze()