class Solution(object):
    def binary_search(self, target,nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1
        while l<=r:
            mid=int((l+r)//2)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return l

obj = Solution()
nums = [1,5,7,9,13,16,20]
target=3
nums = [1,3,5,6]
target = 2
print(obj.binary_search(target,nums))



