def quick_sort(arr,low,high): 
    '''
        1)does inplace sorting, no extra array is taken as in Merge sort
    '''  
    s=low
    e=high
    mid=s+(e-s)//2
    p=arr[mid]

    if low>=high:
        return

    while s<=e:
        while arr[s]< p:
            s+=1
        
        while arr[e]> p:
            e-=1

        if s<=e:
            arr[s],arr[e] = arr[e],arr[s]
            s +=1
            e-=1

    quick_sort(arr,low,e)
    quick_sort(arr,s,high)


arr=[5,3,4,1,2]
quick_sort(arr,0,len(arr)-1)
print(arr)