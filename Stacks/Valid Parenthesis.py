class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        hash={')':'(',']':'[','}':'{'}
        for i in s:
            if i in hash:
                if not stack or stack[-1]!=hash[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        if not stack:
            return True
        return False

obj = Solution()
n = '[()]'
print(obj.isValid(n))