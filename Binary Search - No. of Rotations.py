class Solution(object):
    def binary_search(self, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1
        while l<r:
            mid=int((l+r)//2)
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return [nums[l],l]

obj = Solution()
nums = [2,3,4,1]
print(obj.binary_search(nums))


