from custom_maze import maze
from state import find_neighbors
'''
#import maze array
init_maze=maze
nbors=find_neighbors(init_maze,robo_start)

for i in range(len(init_maze)):
    for j in range(len(init_maze[0])):
        if init_maze[i][j] == 1:
            init_maze[i][j] == 1000
        elif init_maze[i][j]==2
            init_maze[i][j]== 2000
        elif init_maze [i][j]== 3
            init_maze[i][j] ==3000
            

fin_path=path_finder(init_maze)


def path_finder(init_maze):
    maze_start=list(zip(*np.where(init_maze==3000)))
    robo_position=maze_start[0]
    
    for i in range(len(init_maze)):
        for j in range(len(init_maze[0])):
            nbors=find_neighbors(init_maze,robo_position)
            for k in range(len(nbors)):
                x,y=nbors[k]
                if init_maze[i][j]== 0:
                    init_maze[x][y]=1
                elif init_maze[x][y] != init_maze[i][j]+1:
                    init_maze[x][y]=init_maze[i][j]+1
'''






                
                

                





   




