class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """        
        l=r=res=count=0
        min_count=float('inf')

        while r<len(nums):
            res+=nums[r]
            while res>=target and l<=r:
                count=r-l+1
                # print('true',nums[l:r+1],res,count)
                min_count=min(min_count,count)
                res-=nums[l]
                l+=1
                # print('removing',nums[l:r+1],res,count)
            r+=1
        if min_count==float('inf'):
            return 0
        else:
            return min_count

obj = Solution()
target = 7
nums = [2,3,1,2,4,3]

target = 4
nums = [1,4,4]

# target = 11
# nums = [1,1,1,1,1,1,1,1]
print(nums)
print(obj.minSubArrayLen(target, nums))  
