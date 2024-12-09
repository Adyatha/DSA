def Search(matrix, tar):
    rows = len(matrix)
    cols = len(matrix[0])

    #if the matrix has only 1 row
    if rows == 1:
        return binary(matrix,tar,0,0,cols-1)
    
    rstart = 0
    rend = cols-1
    cmid = cols//2

    #shortening the search space

    while rstart<rend-1:
        mid = rstart + (rstart-rend)//2

        if tar==matrix[rstart][cmid]:
            return [rstart,cmid]
        elif tar>matrix[rstart][cmid]:
            rstart=mid+1
        else:
            rend=mid-1
    
    #check for 2 rows mid elems

    if matrix[rstart][cmid] == tar:
        return [rstart,cmid]
    elif matrix[rstart+1][cmid] == tar:
        return [rstart+1,cmid]
    
    # check for 1st half
    if tar<=matrix[rstart][cmid-1]:
        return binary(matrix,tar,rstart,0,cmid-1)
        
    # check for 2nd half
    elif tar>=matrix[rstart][cmid+1] and tar<=matrix[rstart][cols-1]:
        return binary(matrix,tar,rstart,cmid+1,cols-1)

    # check for 3rd half
    elif tar<=matrix[rstart+1][cmid-1]:
        return binary(matrix,tar,rstart+1,0,cmid-1)

    # check for 4th half
    else:
        return binary(matrix,tar,rstart+1,cmid+1,cols-1)



def binary(matrix,tar,row,colstart,colend):
    while(colstart<=colend):
        cmid= colstart +(colstart-colend)//2
        if matrix[row][cmid] == tar:
            return [row,cmid]
        elif matrix[row][cmid] < tar:
            colstart = cmid +1
        else:
            colend = cmid-1
    
    return [-1,-1]


matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
tar = 10
print(Search(matrix,tar))