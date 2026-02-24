class Solution(object):
    def binary_search(self, target,nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1
        min_index=float('inf')
        while l<=r:
            mid=int((l+r)//2)
            if nums[mid]==target:
                min_index=min(min_index,mid)
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return min_index

obj = Solution()
nums = [1,5,6,7,7,9,13,13,13,16,20]
target=13
print(obj.binary_search(target,nums))



