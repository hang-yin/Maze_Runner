import numpy as np
import random
from state import find_all_neighbors, find_wall_neighbors, find_neighbors

def display_maze(maze):
    for k in range(len(maze)):
        print(maze[k])
    print('\n')

def generate_maze():
    n = random.randint(8, 10)   # rows
    m = random.randint(8, 10)   # cols
    print('n: {}, m: {}'.format(n,m))

    maze = []

    for i in range(n):
        row = []
        for j in range(m):
            row.append(1)
        maze.append(row)

    # display_maze()


    # coordinates to start building free cells
    x = random.randint(0, n-1)
    y = random.randint(0, m-1)
    cell_A = (x, y)
    maze[x][y] = 0
    walls = []



    # maze[x][y] = 0  # random cell to start creating free cells with (A)
    neighbors = find_all_neighbors(maze, (x,y))     # returns a list of neighbor coords for A
    for nbr in neighbors:
        walls.append(nbr)   # add all neighbors to wall list

    while len(walls) != 0:
        cell_C = walls[random.randint(0, len(walls)-1)]   # C is a wall

        # check if C is an edge cell
        if cell_C[0] == 0 or cell_C[0] == n-1 or cell_C[1] == 0 or cell_C[1] == m-1:
            walls.remove(cell_C)
            continue

        c_neighbors = find_neighbors(maze, cell_C)
        if len(c_neighbors)>=2:
            walls.remove(cell_C)
            continue
        else:
            cell_A = c_neighbors[0]

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

        if maze[cell_A[0]][cell_A[1]] == 1 or maze[cell_B[0]][cell_B[1]] == 1:
            if maze[cell_A[0]][cell_A[1]] == 1:
                cell_D = cell_A
            else:
                cell_D = cell_B

            # Make C and D free
            maze[cell_C[0]][cell_C[1]] = 0
            maze[cell_D[0]][cell_D[1]] = 0

            neighbors_D = find_wall_neighbors(maze, cell_D)     # returns a list of neighbor coords for D
            for nbr in neighbors_D:
                walls.append(nbr)   # add all wall neighbors of D to wall list

        walls.remove(cell_C)    # remove C from wall list
        #display_maze()

    #display_maze()
    return maze