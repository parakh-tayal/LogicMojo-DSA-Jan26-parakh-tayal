class Solution(object):
    def subarraysum(self, nums,k):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=0
        res=0
        new_arr=[]
        while r<len(nums):
            res+=nums[r]
            if (r-l+1)==k:
                new_arr.append(res)
                res-=nums[l]
                l+=1
            r+=1
        return new_arr
        
obj = Solution()
nums = [1,2,3,4,5,6]
k=3
print(nums)
print(obj.subarraysum(nums,k))
