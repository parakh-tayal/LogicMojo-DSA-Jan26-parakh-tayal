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
            # mid=int(l+(r-l)/2)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return "Not found"

obj = Solution()
nums = [1,5,7,9,13,16,20]
target=13
print(obj.binary_search(target,nums))



