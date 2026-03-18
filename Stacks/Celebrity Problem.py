class Solution(object):
    def IsCelebrity(self, n):
        stack=[i for i in range(len(n))]
        while len(stack)>1:
            a=stack.pop()
            b=stack.pop()
            if self.knows(a,b,n):
                stack.append(b)
            else:
                stack.append(a)
        print(stack)
        candidate=stack.pop()
        for i in range(len(n[0])):
            if (n[i][candidate]==0 or n[candidate][i]==1) and i!=candidate:
                return False
        return candidate
    
    def knows(self,a,b,n):
        if n[a][b]==1:
            return True
        return False

obj = Solution()
n = [[0,0,1,0],[0,0,1,0],[0,0,0,0],[0,0,1,0]]
n = [
 [0,1,1],
 [0,0,1],
 [1,1,0]
]
print(obj.IsCelebrity(n))