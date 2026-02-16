# given a sorted array. create a new array containing squares of all the numbers in the input array in sorted order.

class Solution(object):
    def bruteforce(self,nums):
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums
    
    def twopointers(self,num):
        new_arr=[0]*len(nums)
        l=0
        r=len(nums)-1
        current=len(nums)-1
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                new_arr[current] = nums[l]*nums[l]
                l+=1
            else:
                new_arr[current] = nums[r]*nums[r]
                r-=1
            current-=1
            
        return new_arr
                
obj = Solution()
nums = [-2,-1,0,2,3]
# print(obj.bruteforce(nums))
print(obj.twopointers(nums))
