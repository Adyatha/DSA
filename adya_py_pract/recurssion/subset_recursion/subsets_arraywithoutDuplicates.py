class Solution:
    def subsetswithduplicates(self,nums):
        subset=[]
        res=[]
        
        nums.sort()
        
        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)
            
            subset.pop()
            while i+1<len(nums) and nums[i] == nums[i+1]:
                i+= 1 
            dfs(i+1)
        
        dfs(0)
        return res

if __name__ == "__main__":
    a=Solution()
    nums = [1,1,2]
    print(a.subsetswithduplicates(nums))