def missingNumber(nums):
        i = 0
        while(i < len(nums)):
            correct = nums[i]
            if nums[i] != nums[correct] and nums[i] < len(nums) :
                swap(nums, i, correct)
                print(i,nums)
            else:
                i+=1
        print(nums)
        for j in range(0,len(nums)):
            if nums[j] != j:
                return j
        return len(nums)


def swap(arr,first,second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp
        
arr=[3,0,1]
print(missingNumber(arr))