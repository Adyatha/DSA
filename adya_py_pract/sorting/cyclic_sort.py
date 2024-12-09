def cyclic(arr):
    '''
        1)apply as soon as u see 1 to n elements in the question
        2)not applicable for array with duplicate values
    '''
    i=0
    while( i <len(arr)):
        correct = arr[i]-1
        if arr[i] != arr[correct]:
            swap(arr,i,correct)
        else:
            i+=1
    return arr

def swap(arr,first,second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp


arr = [2,1,5,3,4]
print(cyclic(arr)) 