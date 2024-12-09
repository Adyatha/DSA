def binary_search(arr,tar):
    start=0
    end=len(arr)-1
    while(start <= end):
        mid = start + (end-start)//2
        if tar<arr[mid]:
            end = mid-1
        elif tar > arr[mid]:
            start = mid +1
        else:
            return mid
    return -1

a = [1,4,7,8,9,13,45,90]
tar = 13

res=binary_search(a , tar)
if res != -1:
    print(f"{tar} found at index {res}")
else:
    print(f"{tar} not found")
