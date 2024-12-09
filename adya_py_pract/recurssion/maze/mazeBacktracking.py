def mazeBacktracking(maze,path,r,c):
    if r==len(maze)-1 and c==len(maze[0])-1:
        print(path)
        return
    
    if not maze[r][c]:
        return
    
    maze[r][c]= False

    if r<len(maze)-1:
        mazeBacktracking(maze,path+"D",r+1,c)

    if c<len(maze[0])-1:
        mazeBacktracking(maze,path+"R",r,c+1)

    if r>0:
        mazeBacktracking(maze,path+"U",r-1,c)

    if c>0:
        mazeBacktracking(maze,path+"L",r,c-1)

    maze[r][c]= True



maze=[[True,True,True],
      [True,True,True],
      [True,True,True]]
path=""
mazeBacktracking(maze,path,0,0)
