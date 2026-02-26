# Floor of a value = lower_bound - 1
# Ceil of a value = lower_bound

class Solution(object):
    
    def min_abs_diff(self,target,nums):
        l=0
        r=len(nums)
        while l<r:
            mid=int((l+r)//2)
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid
        
        if l==0:
            return l
        elif l==len(nums):
            return nums[l-1]

        # we are doing floor diff vs ceil diff
        if (abs(nums[l-1]-target)) < (abs(nums[l]-target)):
            return nums[l-1]
        else:
            return nums[l]
        
obj = Solution()
nums = [1,3,8,10,15]
key=14
# nums = [2,3,8,10,15]
# key=1
# op=10
print('Key is '+str(key))
# print(obj.floor_element(key,nums))
# print(obj.ceil_element(key,nums))
print(obj.min_abs_diff(key,nums))



