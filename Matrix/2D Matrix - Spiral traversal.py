"""
 Spiral traversal
"""

def traversal(n):
    for rows in range(len(n)):
        for cols in range(len(n[0])):
            print(n[rows][cols],end=' ')
        print('\n')

def spiral_traversal(n):
    l=0
    r=len(n[0])-1
    t=0
    b=len(n)-1

    while l<=r and t<=b:
        for i in range(l,r+1):
            print(n[t][i])
        t+=1

        for i in range(t,b+1):
            print(n[i][r])
        r-=1

        if t<=b:
            for i in range(r,l-1,-1):
                print(n[b][i])
            b-=1

        if l<=r:
            for i in range(b,t-1,-1):
                print(n[i][l])
            l+=1

n = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# n = [[1,2,3,11],[4,5,6,12],[7,8,9,13],[10,14,15,16]]
n = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9, 10],
    [11,12,13,14,15]
]
traversal(n)
print('---------------------------------')
spiral_traversal(n)
print('---------------------------------')


