class Solution(object):
    def first_binary_search(self, target,nums):
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
    
    def last_binary_search(self, target,nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1
        max_index=float('-inf')
        while l<=r:
            mid=int((l+r)//2)
            if nums[mid]==target:
                max_index=max(max_index,mid)
                l=mid+1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return max_index
    
    def first_last_bs(self,target,nums):
        indexes = [self.first_binary_search(target,nums),self.last_binary_search(target,nums)]
        if indexes==[float('inf'),float('-inf')]:
            return [-1,-1]
        else:
            return indexes

obj = Solution()
nums = [1,5,7,7,7,9,13,13,13,16,20]
target=6
print(obj.first_last_bs(target,nums))



