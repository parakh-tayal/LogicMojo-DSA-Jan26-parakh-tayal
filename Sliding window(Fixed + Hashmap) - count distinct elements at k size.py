"""
Problem: Count Distinct Elements in Every Window

You are given:
integer array nums
integer k

Return an array where each element represents the number of distinct elements in every contiguous subarray (window) of size k.

Example
nums = [1, 2, 1, 3, 4, 2, 3]
k = 4

Windows:

[1,2,1,3] → {1,2,3} → 3
[2,1,3,4] → {1,2,3,4} → 4
[1,3,4,2] → {1,2,3,4} → 4
[3,4,2,3] → {2,3,4} → 3
"""

class Solution(object):
    def distinct_chars(self, s, k):
        l=r=ml=0
        seen={}
        arr=[]
        while r<len(nums):
            seen[nums[r]]=seen.get(nums[r],0)+1
            if r-l+1 > k:
                seen[nums[l]]-=1
                if seen[nums[l]]==0:
                    del seen[nums[l]]
                l+=1
            if r-l+1==k:
                arr.append(len(seen))
            r+=1

        return arr
    
    def distinct_chars_2(self, n, k):
        hash={}
        l=r=0
        while r<k:
            hash[n[r]]=hash.get(n[r],0)+1
            r+=1
        res=[len(hash)]

        while r<len(n):
            hash[n[r]]=hash.get(n[r],0)+1
            hash[n[l]]-=1
            if hash[n[l]]==0:
                del hash[n[l]]
            l+=1
            r+=1
            res.append(len(hash))
        return res


obj = Solution()
nums = [1, 2, 1, 3, 4, 2, 3]
k = 4
print(nums)
print(obj.distinct_chars(nums,k))  
print(obj.distinct_chars_2(nums,k))  
