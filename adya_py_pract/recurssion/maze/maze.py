def maze(p,r,c):
    if r==1 and c==1:
        print(p)
        return
    
    if r>1:
        maze(p+'D',r-1,c)
    if c>1:
        maze(p+'R',r,c-1)
    
maze('',3,3)

