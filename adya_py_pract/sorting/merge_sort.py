def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left_arr=merge_sort(arr[:mid])
    right_arr=merge_sort(arr[mid:])
    return merge(left_arr,right_arr)


def merge(left_arr,right_arr):
    mix_arr=[]
    i=j=0

    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i]<right_arr[j]:
            mix_arr.append(left_arr[i])
            i+=1
        else:
            mix_arr.append(right_arr[j])
            j+=1
        
    mix_arr.extend(left_arr[i:])
    mix_arr.extend(right_arr[j:])

    return mix_arr

arr=[5,3,4,2,1]
s=merge_sort(arr)
print(s)