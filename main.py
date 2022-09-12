from custom_maze import maze
from state import find_neighbors
from user_input import get_start_position, get_goal_position
import sys

# generate maze with prim's algorithm
# maze = generate_maze()

# get maze dimensions
n = len(maze)
m = len(maze[0])

# display maze

# ask for user input on start and goal position
start_row, start_col = get_start_position(maze, n, m)
goal_row, goal_col = get_goal_position(maze, n, m)

# solve maze and print maze along the way!