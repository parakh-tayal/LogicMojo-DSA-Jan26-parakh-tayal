class Solution(object):
    def stock_span(self, n):
        stack=[]
        res=[-1]*len(n)
        for i in range(len(n)-1,-1,-1):
            print(stack)
            while stack and n[i]>n[stack[-1]]:
                res[stack.pop()]=i
            stack.append(i)

            
        for i in range(len(n)):
            res[i]=i-res[i]
        return res

obj = Solution()
n = [100,80,60,70,60,75,85]
n = [100, 80, 80, 80, 70]
[1, 1, 2, 3, 1]
print(obj.stock_span(n))


# logic - 6 min
# code - 12-6=6 mins
# total - 6 minutes


