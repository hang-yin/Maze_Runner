from custom_maze import maze

def find_neighbors(maze, position):
    n = len(maze)
    m = len(maze[0])
    x0,y0 = position
    neighbors = []
    for x1,y1 in [(x0-1,y0),(x0+1,y0),(x0,y0-1),(x0,y0+1)]:
        if x1>=0 and x1<n and y1>=0 and y1<m and (maze[x1][y1]==0 or maze[x1][y1]==2):
            neighbors.append((x1,y1))
    return neighbors

def find_neighbors_belief(maze, position):
    n = len(maze)
    m = len(maze[0])
    x0,y0 = position
    neighbors = []
    for x1,y1 in [(x0-1,y0),(x0+1,y0),(x0,y0-1),(x0,y0+1)]:
        if x1>=0 and x1<n and y1>=0 and y1<m and (maze[x1][y1]==0 or maze[x1][y1]==2):
            neighbors.append((x1,y1))
    return neighbors

def find_neighbors_dfs(maze, position):
    n = len(maze)
    m = len(maze[0])
    x0,y0 = position
    neighbors = []
    for x1,y1 in [(x0-1,y0),(x0+1,y0),(x0,y0-1),(x0,y0+1)]:
        if x1>=0 and x1<n and y1>=0 and y1<m and (maze[x1][y1]==0 or maze[x1][y1]==3):
            neighbors.append((x1,y1))
    return neighbors

def find_all_neighbors(maze, position):
    n = len(maze)
    m = len(maze[0])
    x0,y0 = position
    neighbors = []
    for x1,y1 in [(x0-1,y0),(x0+1,y0),(x0,y0-1),(x0,y0+1)]:
        if x1>=0 and x1<n and y1>=0 and y1<m:
            neighbors.append((x1,y1))
    return neighbors


def find_wall_neighbors(maze, position):
    n = len(maze)
    m = len(maze[0])
    x0,y0 = position
    neighbors = []
    for x1,y1 in [(x0-1,y0),(x0+1,y0),(x0,y0-1),(x0,y0+1)]:
        if x1>=0 and x1<n and y1>=0 and y1<m and maze[x1][y1]==1:
            neighbors.append((x1,y1))
    return neighbors