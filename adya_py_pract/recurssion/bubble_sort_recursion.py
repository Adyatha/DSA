def bubble(arr, row , col):
    if row == 0:
        return 
    if col < row-1:
        if arr[col]>arr[col+1]:
            arr[col] , arr[col+1] = arr[col+1],arr[col]
        bubble(arr,row , col+1)
    else:
        bubble(arr,row-1 , 0)

arr=[4,6,7,1]
bubble(arr,len(arr),0)
print(arr)