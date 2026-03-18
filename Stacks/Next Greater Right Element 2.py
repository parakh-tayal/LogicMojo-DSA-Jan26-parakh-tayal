class Solution(object):
    def NGR_2(self, n):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        res=[-1]*len(n)
        for i in range(2*len(n)-1,-1,-1):
            num=i%len(n)
            while stack and stack[-1]<=n[num]:
                stack.pop()

            if stack and i<len(n):
                res[i]=stack[-1]
            
            stack.append(n[num])
        return res
    
    def NGR(self, n):
        stack=[]
        res=[-1]*len(n)

        for i in range(len(n)):
            while stack and n[i]>n[stack[-1]]:
                res[stack.pop()]=n[i]
            stack.append(i)
        return res
    

obj = Solution()
n = [4,5,2,1]
# n = [4,2,3,10]
# n = [2,3,2,10]
print(obj.NGR(n))
print(obj.NGR_2(n))
