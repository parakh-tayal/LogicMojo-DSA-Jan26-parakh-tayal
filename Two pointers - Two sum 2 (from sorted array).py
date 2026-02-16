# given a sorted array. find indices of 2 elements whose sum = target

class Solution(object):
    def bruteforce(self,nums,target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
    
    def twopointers(self,num,target):
        l=0
        r=len(nums)-1
        while l<r:
            res=nums[l]+nums[r]
            if res==target:
                return [l,r]
            elif res<target:
                l+=1
            else:
                r-=1
        return "Not found"
                

obj = Solution()
nums = [2,7,9,11,15]
target = 11
# nums = [-1,-1,-1,-1,-1,1,1]
# target = 2
# print(obj.bruteforce(nums,target))
print(obj.twopointers(nums,target))
