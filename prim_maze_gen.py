import numpy as np
import random

m = random.randint(4, 10)   # rows
n = random.randint(4, 10)   # cols
print('m: {}, n: {}'.format(m,n))

maze = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(1)
    maze.append(row)

for k in range(m):
    print(maze[k])


# coordinates for building free cells
a = random.randint(0, m-1)
b = random.randint(0, n-1)

maze[a[b]] = 0