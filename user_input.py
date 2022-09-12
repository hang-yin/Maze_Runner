import sys

def get_start_position(maze, n, m):

    x0 = int(input("Which row should our robot be on?\n"))
    if x0 < 0 or x0 >= n:
        print("Invalid row number: should be between 0 and n\n")
        x0,y0 = get_start_position(maze, n, m)
        return (x0,y0)
    
    y0 = int(input("Which column should our robot be on?\n"))
    if y0 < 0 or y0 >= m:
        print("Invalid column number: should be between 0 and m\n")
        x0,y0 = get_start_position(maze, n, m)
        return (x0,y0)
    
    if maze[x0][y0]==1:
        print("Invalid position: you can not start on a wall cell\n")
        x0,y0 = get_start_position(maze, n, m)
        return (x0,y0)

    return (x0,y0)

def get_goal_position(maze, n, m):

    x1 = int(input("Which row should our robot get to?\n"))
    if x1 < 0 or x1 >= n:
        print("Invalid row number: should be between 0 and n\n")
        x1, y1 = get_goal_position(maze, n, m)
        return (x1,y1)
    y1 = int(input("which column should our robot get to?\n"))
    if y1 < 0 or y1 >= m:
        print("Invalid column number: should be between 0 and m\n")
        x1, y1 = get_goal_position(maze, n, m)
        return (x1,y1)
    
    if maze[x1][y1]==1:
        print("Invalid position: you can not end on a wall cell\n")
        x1, y1 = get_goal_position(maze, n, m)
        return (x1,y1)

    return (x1,y1)