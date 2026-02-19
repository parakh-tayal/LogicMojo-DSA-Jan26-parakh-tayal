# given a sorted array. create a new array containing squares of all the numbers in the input array in sorted order.

class Solution(object):
    def bruteforce(self,nums):
        max_area = float('-inf')
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                l=min(nums[i],nums[j])
                b=j-i
                area = l*b
                max_area = max(max_area,area)
        return max_area
    
    def twopointers(self,nums):
        i=0
        j=len(nums)-1
        max_area = float('-inf')
        while i<j:
            l=min(nums[i],nums[j])
            b=j-i
            area = l*b
            max_area = max(max_area,area)

            if nums[i]<nums[j]:
                i+=1
            else:
                j-=1
        return max_area

obj = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(obj.bruteforce(height))
print(obj.twopointers(height))


