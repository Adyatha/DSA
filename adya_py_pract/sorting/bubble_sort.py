def bubble(arr):
    for i in range(len(arr)-1):
        swapped = False
        for j in range(1,len(arr)-i):
            if arr[j-1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
                swapped = True
        
        if swapped == False:
            break
    return arr

      