import pygame
from pygame.locals import *
from custom_maze import maze
from state import find_neighbors
from user_input import get_start_position, get_goal_position
#from maze_solver import path_finder
from wavefront import wavefront
from recursive_backtracking import recursive_backtracking
from belief_state import beliefstate
from prim_maze_gen import generate_maze, display_maze

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (138, 43, 226)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
ORANGE = (255,165,0)

# generate maze
maze = generate_maze()
grid = maze
n = len(grid)
m = len(grid[0])

# get user input on start and goal position
display_maze(maze)
#t = threading.Thread(target=target_function)
# start_row, start_col = get_start_position(maze, n, m)
goal_row, goal_col = get_goal_position(maze, n, m)
# maze[start_row][start_col] = 2
maze[goal_row][goal_col] = 3
# robot_pos = (start_row,start_col)
robot_pos = (goal_row, goal_col)
# run maze solver HERE
# robot_pos = (3,4)

# solve the maze here
#path = wavefront(maze, (start_row,start_col),(goal_row,goal_col))
#path = set(path)
#path_dfs = recursive_backtracking(maze, (start_row,start_col),(goal_row,goal_col))
#ath_dfs = set(path_dfs)
distance_map = beliefstate(maze, (goal_row, goal_col))
max_distance = max(max(x) for x in distance_map)
distance_set = set()
for i in range(len(distance_map)):
    for j in range(len(distance_map[0])):
        if distance_map[i][j] != -1:
            distance_set.add((i,j))
# range is from 0 to max_distance, which will be mapped to (0,70,0),(0,255,0)

# path = path_solver(maze)
# path = set(path)
# path = set()

# initialize pygame
pygame.init()
WINDOW_SIZE = [800, 800]
num_of_rows = n+1
num_of_cols = m+1
edge = min(WINDOW_SIZE[0]/(num_of_cols+1), WINDOW_SIZE[1]/(num_of_rows+1))
WIDTH = HEIGHT = edge
MARGIN = edge/max(num_of_cols,num_of_rows)
screen = pygame.display.set_mode(WINDOW_SIZE)

done = False
clock = pygame.time.Clock()
grid = maze
 
# main pygame loop
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == K_DOWN:
                if robot_pos[0]+1 < n and maze[robot_pos[0]+1][robot_pos[1]]!=1:
                    robot_pos = (robot_pos[0]+1,robot_pos[1])
            if event.key == K_UP:
                if robot_pos[0]-1 >= 0 and maze[robot_pos[0]-1][robot_pos[1]]!=1:
                    robot_pos = (robot_pos[0]-1,robot_pos[1])
            if event.key == K_LEFT:
                if robot_pos[1]-1 >= 0 and maze[robot_pos[0]][robot_pos[1]-1]!=1:
                    robot_pos = (robot_pos[0],robot_pos[1]-1)
            if event.key == K_RIGHT:
                if robot_pos[1]+1 < m and maze[robot_pos[0]][robot_pos[1]+1]!=1:
                    robot_pos = (robot_pos[0],robot_pos[1]+1)
                #pos = pygame.mouse.get_pos()
                #row = pos[1]
                # grid[row][column] = 5
                #print("Click ", pos, "Grid coordinates: ", row, column)
 
    # Set the screen background
    screen.fill(PURPLE)
 
    # Draw the grid
    for row in range(n):
        for column in range(m):
            color = WHITE
            if grid[row][column] == 1:
                color = BLACK
            elif row == robot_pos[0] and column == robot_pos[1]:
                color = BLUE
            # elif grid[row][column] == 2:
                # color = GREEN
            elif grid[row][column] == 3:
                color = RED
            elif (row, column) in distance_set:
                color = (0, int(((255-70)/max_distance)*(distance_map[row][column]) +70), 0)
            # elif (row, column) in path_dfs:
                # color = ORANGE
            # elif (row, column) in path:
                # color = YELLOW
            
            
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN + edge/2,
                              (MARGIN + HEIGHT) * row + MARGIN + edge/2,
                              WIDTH,
                              HEIGHT])
    
    # Limit to 60 frames per second
    clock.tick(60)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
        
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()