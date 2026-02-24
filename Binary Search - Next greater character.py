class Solution(object):
    def next_greater_char(self, target,nums):
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
            if (nums[mid])>=target:
                min_index=min(min_index,mid)
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        if min_index==float('inf'):
            return -1
        else:
            return chr(nums[min_index])
        # if min_index==float('inf'):
        #     return 'No greater char present'
        # else:
        #     return [min_index,chr(nums[min_index])]

obj = Solution()
chars = ['c','f','k']
target='a'
print((ord(target),[ord(i) for i in chars]))
print(obj.next_greater_char(ord(target),[ord(i) for i in chars]))
