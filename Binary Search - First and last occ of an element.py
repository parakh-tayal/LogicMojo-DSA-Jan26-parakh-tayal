class Solution(object):
    # V1 - Using the Exact match approach

    # def first_binary_search(self, target,nums):
    #     """
    #     :type target: int
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     l=0
    #     r=len(nums)-1
    #     min_index=float('inf')
    #     while l<=r:
    #         mid=int((l+r)//2)
    #         if nums[mid]==target:
    #             min_index=min(min_index,mid)
    #             r=mid-1
    #         elif nums[mid]<target:
    #             l=mid+1
    #         else:
    #             r=mid-1
    #     return min_index
    
    # def last_binary_search(self, target,nums):
    #     """
    #     :type target: int
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     l=0
    #     r=len(nums)-1
    #     max_index=float('-inf')
    #     while l<=r:
    #         mid=int((l+r)//2)
    #         if nums[mid]==target:
    #             max_index=max(max_index,mid)
    #             l=mid+1
    #         elif nums[mid]<target:
    #             l=mid+1
    #         else:
    #             r=mid-1
    #     return max_index
    
    # def first_last_bs(self,target,nums):
    #     indexes = [self.first_binary_search(target,nums),self.last_binary_search(target,nums)]
    #     if indexes==[float('inf'),float('-inf')]:
    #         return [-1,-1]
    #     else:
    #         return indexes

    # ---------------------------------------------------------------------------------------------------------------

    # V2 - using the boundary approach
    def lower_bound(self,target,nums):
        l=0
        r=len(nums)
        while l<r:
            mid=int((l+r)//2)
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid
        return l
    
    def upper_bound(self,target,nums):
        l=0
        r=len(nums)
        while l<r:
            mid=int((l+r)//2)
            if nums[mid]<=target:
                l=mid+1
            else:
                r=mid
        return l
        
    def occ(self,target,nums):
        lower = self.lower_bound(target,nums)
        upper = self.upper_bound(target,nums)

        if lower==len(nums) or nums[lower]!=target:
            return [-1,-1]
        else:
            return [lower,upper-1]
        
    
obj = Solution()
nums = [3,5,7,7,7,9,13,13,13,16,20]
target=7
# print(obj.first_last_bs(target,nums))
print(obj.lower_bound(target,nums))
print(obj.upper_bound(target,nums))
print(obj.occ(target,nums))


