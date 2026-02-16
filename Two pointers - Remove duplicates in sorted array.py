# Given a sorted array, remove all duplicates. You should NOT use any extra space

class Solution(object):
    def removeDuplicates_stack(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # TC O(n),SC O(1) and TC(deletion) O(1)
        curr=len(nums)-1
        while curr>=0:
            if nums[curr]==nums[curr-1]:
                nums.pop(curr)
            curr-=1
        return nums
    
    def removeDuplicates_2pointer_with_On_space(self, nums):
        # NOT IMPORTANT
         # TC O(n),SC O(n)
        r=1
        new_arr=[nums[0]]
        while r<len(nums):
            if nums[r]!=nums[r-1]:
                new_arr.append(nums[r])
            l=r
            r+=1
        return new_arr
    
    def removeDuplicates_2pointer_without_On_space(self, nums):
         # TC O(n),SC O(1) and TC(deletion) O(n)
        r=0
        while r<len(nums)-1:
            if nums[r]==nums[r+1]:
                nums.remove(nums[r+1])
            else:
                r+=1
        return nums

# IMP: Don't use extra space. Do it in in-place with O(1) extra memory.
obj = Solution()
nums=[1,1,2,2,3,4,5,5,5]
print(obj.removeDuplicates_stack(nums))
print(obj.removeDuplicates_2pointer_with_On_space(nums))
print(obj.removeDuplicates_2pointer_without_On_space(nums))