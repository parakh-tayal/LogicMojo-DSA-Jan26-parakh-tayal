class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=r=count_zeroes=0
        max_count=float('-inf')
        # max_l_r=[]
        while r<len(nums):
            if nums[r]==0:
                count_zeroes+=1
            while count_zeroes>k:
                if nums[l]==0:
                    count_zeroes-=1
                l+=1
            max_count=max(max_count,r-l+1)
            r+=1
        return max_count
        #     if max_count<r-l+1:
        #         max_l_r = [l,r+1]
        #         max_count=count
        #     r+=1
        # return [max_count,max_l_r,nums[max_l_r[0]:max_l_r[1]]]


obj = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print(nums)
print(obj.longestOnes(nums,k))
