class Solution(object):
    def first_bs(self,target,nums):
        l=0
        r=len(nums)-1
        x=-1
        while l<=r:
            mid=int((l+r)//2)
            if nums[mid]==target:
                x=mid
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return x
    
    def last_bs(self,target,nums):
        l=0
        r=len(nums)-1
        x=-1
        while l<=r:
            mid=int((l+r)//2)
            if nums[mid]==target:
                x=mid
                l=mid+1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return x
    
    def frequency_of_element(self,target,nums):
        indexes = [self.first_bs(target,nums),self.last_bs(target,nums)]
        indexes = [0 if i==-1 else i for i in indexes]
        print(indexes)
        if indexes[0]==indexes[1]==0:
            return 0
        else:
            return indexes[1]-indexes[0]+1
        
    # ---------------------------------------------------------------------------------------------------------------

    # V2 - using the boundary approach
    # def lower_bound(self,target,nums):
    #     l=0
    #     r=len(nums)
    #     while l<r:
    #         mid=int((l+r)//2)
    #         if nums[mid]<target:
    #             l=mid+1
    #         else:
    #             r=mid
    #     return l
    
    # def upper_bound(self,target,nums):
    #     l=0
    #     r=len(nums)
    #     while l<r:
    #         mid=int((l+r)//2)
    #         if nums[mid]<=target:
    #             l=mid+1
    #         else:
    #             r=mid
    #     return l
        
    # def occ(self,target,nums):
    #     lower = self.lower_bound(target,nums)
    #     upper = self.upper_bound(target,nums)

    #     if lower==len(nums) or nums[lower]!=target:
    #         return 0
    #     else:
    #         return upper-lower


obj = Solution()
nums = [1,5,7,7,7,9,13,13,13,13,16,20]
target=6
print(obj.first_bs(target,nums))
print(obj.last_bs(target,nums))
print(obj.frequency_of_element(target,nums))




