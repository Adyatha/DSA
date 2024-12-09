def insertion(arr):
    ''' 1)It is a stable sorting Algorithm - inplace sorting
        2)Used mostly in hybrid sorting Algorithm like merge sort and quick sort
        3)uses O(n**2) time complexity
    
    '''
    for i in range(0,len(arr)-1):
        for j in range(i+1,0,-1):
            if arr[j]<arr[j-1]:
                t = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = t
    return arr

print(insertion.__doc__)
arr = [2,1,5,3,4,4]
print(insertion(arr)) 


