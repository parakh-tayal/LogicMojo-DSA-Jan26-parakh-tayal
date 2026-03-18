class Solution(object):
    # using stack application
    # def largest_rectangle_histogram(self, n):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     max_area=0
    #     for i in range(len(n)):
    #         l=self.NSL(n,i)
    #         r=self.NSR(n,i)
    #         # print(n[i],l)
    #         if len(n)==1:
    #             w=r-l
    #         else:
    #             w=r-l-1
    #         h=n[i]
    #         area=h*w
    #         print(n[i],l,r,'area -',area,'w -',w,'h -',h)
    #         max_area=max(max_area,area)
    #     return max_area
        
    # def NSL(self,n,n_index):
    #     last_val=0
    #     k=n[n_index]
    #     for i in range(n_index,-1,-1):
    #         if n[i]<k:
    #             last_val=i
    #             return last_val
    #     print(last_val)
    #     return last_val
    
    # def NSR(self,n,n_index):
    #     last_val=0
    #     k=n[n_index]
    #     for i in range(n_index,len(n)):
    #         if n[i]<k:
    #             last_val=i
    #             return last_val
    #         elif i==len(n)-1:
    #             last_val=i+1
    #     return last_val


    def largest_rectangle_histogram(self, heights):
        n=heights
        l=self.NSL(n)
        r=self.NSR(n)
        print(l,r)
        max_area=0
        for i in range(len(n)):
            w = r[i]-l[i]-1
            h=n[i]
            area=w*h
            max_area=max(max_area,area)
        return max_area
    
    def NSR(self,n):
        stack=[]
        res=[len(n)]*len(n)
        for i in range(len(n)):
            while stack and n[i]<n[stack[-1]]:
                res[stack.pop()]=i
            stack.append(i)
        return res
    
    def NSL(self,n):
        stack=[]
        res=[-1]*len(n)
        for i in range(len(n)-1,-1,-1):
            while stack and n[i]<n[stack[-1]]:
                res[stack.pop()]=i
            stack.append(i)
        return res
        
obj = Solution()
n = [2,1,5,6,2,3]
# n = [2,4]
# n = [1]
# n = [1,1]
# n = [2,1,2]
print(n)
print(obj.largest_rectangle_histogram(n))
