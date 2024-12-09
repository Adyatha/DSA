
def flipAndInvertImage(image):
    n= len(image)
    reverse=[[0]*n for _ in range(n) ]
    ans =[[0]*n for _ in range(n) ]
    
    for i in range(n):
        for j in range(n):
            reverse[i][j] = image[i][n-j-1]
    
    for i in range(n):
        for j in range(n):
            if reverse[i][j] == 0:
                ans[i][j] = 1
            else:
                ans[i][j] = 0
    return ans
                
image=[[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(image))
# [[1,0,0],[0,1,0],[1,1,1]]