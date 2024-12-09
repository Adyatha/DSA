def display(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i][j]):
                print("Q", end=" ")
            else:
                print("X", end=" ")
        print()
    print()


def queens(board,row):
    if row == len(board):
        display(board)
        return 1
    
    count=0
    
    for i in range(0,len(board)):
        if isSafe(board,row,i):
            board[row][i] = True
            count += queens(board,row+1)
            board[row][i] = False

    return count
    


def isSafe(board,row,col):

    # moving vertically
    for i in range(0,row):
        if board[i][col]:
            return False
        
    # diagonal left
    maxleft= min(row,col)
    for i in range(1,maxleft+1):
        if board[row-i][col-i]:
            return False
        
    # diagonal right
    
    maxright= min(row,len(board)-col-1)
    for i in range(1,maxright+1):
        if board[row-i][col+i]:
            return False
        
    return True


n=4
board = [[False for j in range(n)]for i in range(n)]
print("total sol:",queens(board,0))