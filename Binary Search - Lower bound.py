# Search Insert position

# Lower bound is boundary search
# Lower bound is used to find first occ of an element
# Lower bound will always provide index of an element where it should be inserted in sorted way
        # if we have duplicates then it will insert BEFORE like _,2,2,2
                                                # And for UPPER   2,2,2,_
# Lower bound will always provide either EXACT MATCH or CEIL of an element
# Ceil of a value = lower_bound

class Solution(object):
    def lower_bound(self, target,nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)
        while l<r:
            mid=int((l+r)//2)
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid
        return l


obj = Solution()
# nums = [1,5,7,9,13,16,20]
# target=16
nums = [1,2,2,3,5,6]
target = 2
print(obj.lower_bound(target,nums))



