class Solution(object):
    def binary_search(self, nums,target):
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
            
            if nums[l]<=nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1

obj = Solution()
nums = [8,9,1,2,3,4,5,6,7]
target=5
print(obj.binary_search(nums,target))


