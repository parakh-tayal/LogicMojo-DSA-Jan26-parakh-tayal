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
        max_sum=float('-inf')
        while r<len(nums):
            res+=nums[r]
            if (r-l+1)==k:
                max_sum=max(max_sum,res)
                res-=nums[l]
                l+=1
            r+=1
        return max_sum
        
obj = Solution()
nums = [1,0,8,2,3]
k=2
print(nums)
print(obj.subarraysum(nums,k))
