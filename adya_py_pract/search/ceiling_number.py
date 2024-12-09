def ceiling_num(arr, tar):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start + (end-start)//2
        if tar < arr[mid]:
            end = mid-1
        elif tar > arr[mid]:
            start = mid+1
        else:
            return arr[mid]
    return arr[start]

arr = [3,9,23]
tar = 22
res = ceiling_num(arr, tar)

print(f"the ceiling of {tar} is {res}")
