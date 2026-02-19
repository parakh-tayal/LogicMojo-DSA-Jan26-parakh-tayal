class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=0
        r=0
        while r<len(nums):
            print(nums)
            if nums[r]!=0:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
            r+=1
        return nums

obj = Solution()
nums = [0,1,0,3,12]
# nums = [2,1]
print(obj.moveZeroes(nums))