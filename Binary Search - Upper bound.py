# Search Insert position

# Upper bound is boundary search
# Upper bound is used to find filastrst occ of an element
# Upper bound will always provide index of an element where it should be inserted in sorted way
        # if we have duplicates then it will insert BEFORE like _,2,2,2       => for lower
                                                # And for UPPER   2,2,2,_

class Solution(object):
    def upper_bound(self, target,nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)
        while l<r:
            mid=int((l+r)//2)
            if nums[mid]<=target:
                l=mid+1
            else:
                r=mid
        return l


obj = Solution()
# nums = [1,5,7,9,13,16,20]
# target=16
nums = [1,2,2,2,2,3,5,6]
target = 5
print(obj.upper_bound(target,nums))



