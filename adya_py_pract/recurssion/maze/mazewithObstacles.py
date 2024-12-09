# maze with obstacles

def mazewithObstacles(maze,path,r,c):
    if r==len(maze)-1 and c==len(maze[0])-1:
        print(path)
        return
    
    if not maze[r][c]:
        return
    
    if r<len(maze)-1 and c<len(maze[0])-1:       # moving diagonally
        mazewithObstacles(maze,path+"D",r+1,c+1)

    if r<len(maze)-1:
        mazewithObstacles(maze,path+"V",r+1,c)

    if c<len(maze[0])-1:
        mazewithObstacles(maze,path+"H",r,c+1)



maze=[[True,True,True],
      [True,False,True],
      [True,True,True]]
path=""
mazewithObstacles(maze,path,0,0)
