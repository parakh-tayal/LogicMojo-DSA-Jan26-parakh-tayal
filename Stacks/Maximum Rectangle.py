"""
85. Maximal Rectangle-Hard

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:
Input: matrix = [[0,0,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: 6

my logic is if calculate this matrix of n*n and convert it into single array by progressively calculating height 
so, res_arr will become [0,3,4,0] and if i apply area of histogram approach here by finding NSL and NSR. Will it be resolved? Is my solution correct?

Leetcode - Hard
"""

"""
Solution

for each row:
    update heights
    compute histogram area
    update max

"""

class Solution(object):

    def maximum_rectangle(self, n):
        max_area=0
        heights=[0]*len(n[0])
        for i in range(len(n)):
            for j in range(len(n[0])):
                if int(n[i][j])==1:
                    heights[j]+=1
                else:
                    heights[j]=0
            print(heights)
            max_area=max(max_area,self.area_histogram(heights))
        return max_area
    
    def area_histogram(self,n):
        l=self.NSL(n)
        r=self.NSR(n)
        print(l,r)
        max_area=0
        for i in range(len(n)):
            w = r[i]-l[i]-1
            h=n[i]
            print(w,h)
            area=w*h
            max_area=max(max_area,area)
        return max_area
    
    def NSR(self,n):
        stack=[]
        res=[len(n)]*len(n)
        for i in range(len(n)):
            while stack and n[stack[-1]]>n[i]:
                res[stack.pop()]=i
            stack.append(i)
        return res

    def NSL(self,n):
        stack=[]
        res=[-1]*len(n)
        for i in range(len(n)-1,-1,-1):
            while stack and n[stack[-1]]>=n[i]:
                res[stack.pop()]=i
            stack.append(i)
        return res
        

obj = Solution()
n = [[0,0,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# n = [[1,1,0],[1,0,0],[0,0,0]]
n=[["1","0","1","0","0"],
   ["1","0","1","1","1"],
   ["1","1","1","1","1"],
   ["1","0","0","1","0"]]
# print(obj.maximum_rectangle(n))
print(obj.area_histogram([3, 1, 3, 2, 2]))
