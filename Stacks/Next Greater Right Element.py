class Solution(object):
    def NGR(self, n):
        """
        :type s: str
        :rtype: str
        """
        
        # stack=[]
        # hash={i:-1 for i in n}

        # for i in n:
        #     while stack and i>stack[-1]:
        #         hash[stack.pop()]=i
        #     stack.append(i)
        # return [hash[i] for i in n]
    
        # -----------------------------------------------------
        # NGR
        stack=[]
        res=[-1]*len(n)

        for i in range(len(n)):
            while stack and n[i]>n[stack[-1]]:
                res[stack.pop()]=n[i]
            stack.append(i)
        return res
    
    def NGL(self, n):
        stack=[]
        res=[-1]*len(n)

        for i in range(len(n)-1,-1,-1):
            while stack and n[i]>n[stack[-1]]:
                res[stack.pop()]=n[i]
            stack.append(i)
        return res
    
    def NSR(self, n):
        stack=[]
        res=[-1]*len(n)

        for i in range(len(n)):
            while stack and n[i]<=n[stack[-1]]:
                res[stack.pop()]=n[i]
            stack.append(i)
        return res
    
    def NSL(self, n):
        stack=[]
        res=[-1]*len(n)

        for i in range(len(n)-1,-1,-1):
            while stack and n[i]<=n[stack[-1]]:
                res[stack.pop()]=n[i]
            stack.append(i)
        return res

obj = Solution()
n = [4,5,2,10]
n = [4,2,3,10]
# n = [2,3,2,10]
print(obj.NGR(n))
print(obj.NGL(n))
print(obj.NSR(n))
print(obj.NSL(n))