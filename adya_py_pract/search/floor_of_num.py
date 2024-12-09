def floor_num(arr, tar):
    start = 0
    end = len(arr)

    while start <= end:
        mid = start + (end-start)//2
        if tar < arr[mid]:
            end = mid-1
        elif tar > arr[mid]:
            start = mid+1
        else:
            return mid
    return end

arr = [3,9,23]
tar = 2
res = floor_num(arr, tar)

if res != -1:
    print(f"the floor of {tar} is {res}")
else:
    print("no match found")


