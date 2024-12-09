def searching(arr, target, index):
    if index == len(arr):
        return -1
    elif arr[index] == target:
        return index
    else:
        return searching(arr, target, index+1)
    
arr = [1,34,56,23,5]
print(searching(arr,23,0))
print("in 2nd array")
print(searching(arr,6,0))