from custom_maze import maze
from state import find_neighbors, find_neighbors_dfs
from user_input import get_start_position

def recursive_backtracking(maze, start_pos, goal_pos): 
    def dfs(curr_pos, curr_path):
        nonlocal goal_pos
        nonlocal visited
        nonlocal valid_paths
        if curr_pos == goal_pos:
            #print("********")
            curr_path.append(curr_pos)
            valid_paths = curr_path
            return
        #print(curr_pos)
        visited.add(curr_pos)
        neighbours = find_neighbors_dfs(maze, curr_pos)
        for neighbour in neighbours:
            if neighbour not in visited:
                new_path = curr_path[:]
                new_path.append(neighbour)
                dfs(neighbour, new_path)
        #take the current_pos
    visited = set()
    valid_paths = None
    dfs(start_pos, [])
    return valid_paths