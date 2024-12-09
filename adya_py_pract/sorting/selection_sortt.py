def selection(arr):
    for i in range(len(arr)):
        last = len(arr) - i -1
        maxInd = getmaxIndex(arr,0,last)
        swap(arr,maxInd,last)
    return arr

def getmaxIndex(arr,start,last):
    max = start 
    for i in range(start,last+1):
        if arr[max]<arr[i]:
            max = i
    return max

def swap(arr, first , last):
    temp = arr[first]
    arr[first] = arr[last]
    arr[last] = temp

arr = [2,1,5,3,4,1]
print(selection(arr))
