def binary2D(matrix,target):
    r=0
    c=len(matrix)-1

    while(r<len(matrix) and c>=0):
        if (matrix[r][c]==target):
            return [r,c]
        
        elif matrix[r][c] >target:
            c-=1
        else:
            r+=1

    return [-1,-1]

matrix=[[1,2,34,66],[4,5,35,67],[7,8,36,68]]
tar=38
print(binary2D(matrix,tar))