def mazeBacktracking(maze,path,r,c,route,steps):
    if r==len(maze)-1 and c==len(maze[0])-1:
        route[r][c]= steps
        for i in route:
            print(i)
        print(path,"\n")
        # print()
        return
    
    if not maze[r][c]:
        return
    
    maze[r][c]= False
    route[r][c]= steps

    if r<len(maze)-1:
        mazeBacktracking(maze,path+"D",r+1,c,route,steps+1)

    if c<len(maze[0])-1:
        mazeBacktracking(maze,path+"R",r,c+1,route,steps+1)

    if r>0:
        mazeBacktracking(maze,path+"U",r-1,c,route,steps+1)

    if c>0:
        mazeBacktracking(maze,path+"L",r,c-1,route,steps+1)

    maze[r][c]= True
    route[r][c]=0



maze=[[True,True,True],
      [True,True,True],
      [True,True,True]]
path=""
route=[[0 for j in range(len(maze[0]))]for i in range(len(maze))]
steps=1
mazeBacktracking(maze,path,0,0,route,steps)
