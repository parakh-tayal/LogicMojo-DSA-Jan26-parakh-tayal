class Solution(object):
    def duplicate_number_1(self, n):
        # This is same as detecting cycle in LinkedList
        # using Floyd's Algo 1 & 2
        # We have only positive integers here & there is definite gurrantee of duplicate in the list
        # NOTE: This approach is very constraints specific approach

        slow = n[0]
        fast = n[n[0]]

        while True:
            slow = n[slow]
            fast = n[n[fast]] 
            if slow==fast:
                break
        
        start=0
        while slow!=start:
            slow=n[slow]
            start=n[start]
        return slow
    
    def duplicate_number_2(self, n):
        # using hashset
        hashset = set()
        for i in n:
            if i in hashset:
                return i
            else:
                hashset.add(i)
    
    def duplicate_number_3(self,n):
        # using approach of *Finding first positive missing integer*
        # cyclic sort
        i = 0
        while i < len(n):
            correct = n[i] - 1
            if n[i] != n[correct]:
                n[i], n[correct] = n[correct], n[i]
            else:
                if i != correct:    # same value, different index = duplicate!
                    return n[i]
                i += 1
        return -1

obj = Solution()
n = [1,3,4,2,2]
# n = [3]*5
print(obj.duplicate_number_1(n))
print(obj.duplicate_number_2(n))
print(obj.duplicate_number_3(n))



