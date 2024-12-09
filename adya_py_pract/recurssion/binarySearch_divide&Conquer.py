def binary_search(arr,tar, s,e):
    mid=s+(e-s)//2
    if(s>e):
        return -1
    if arr[mid]== tar:
        return mid
    if tar<arr[mid]:
        return binary_search(arr,tar,s,mid-1)
    return binary_search(arr,tar,mid+1,e)

arr = [1,55,56,78,99,102]
tar =54
print(binary_search(arr,tar,0,len(arr)-1))