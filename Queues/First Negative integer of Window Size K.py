from collections import deque

def firstNegInt(n,k):
    q=deque()
    l=r=0

    while r<k-1:
        if n[r]<0:
            q.append(n[r])
        r+=1
    
    while r<len(n):
        if n[r]<0:
            q.append(n[r])

        if q:
            print(q[0])
        else:
            print(0)

        if n[l]<0:
            q.popleft()
        
        l+=1
        r+=1

n = [30,-1,-7,10,2,-15,9,10,11]
n = [12,-1,-7,8,-15,30,16,28]
k=3
firstNegInt(n,k)