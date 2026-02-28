"""
 Spiral 3 traversal - Returns array
"""

def traversal(n):
    for rows in range(len(n)):
        for cols in range(len(n[0])):
            print(n[rows][cols],end=' ')
        print('\n')

def spiral_3_traversal(n,rows,cols,cstart,rstart):
    steps=1
    tc=0
    d=1
    direction_change=0
    arr=[]

    if 0<=rstart<rows and 0<=cstart<cols:
        print(n[rstart][cstart])
        tc+=1

    while tc<rows*cols:
        if d==1:
            # right
            for i in range(steps):
                # ignoring outbound coordinates
                cstart+=1
                if 0<=rstart<rows and 0<=cstart<cols:
                    print(n[rstart][cstart])
                    tc+=1
            d+=1
        elif d==2:
            # down
            for i in range(steps):
                rstart+=1
                if 0<=rstart<rows and 0<=cstart<cols:
                    print(n[rstart][cstart])
                    tc+=1
            d+=1
        elif d==3:
            # left
            for i in range(steps):
                cstart-=1
                if 0<=rstart<rows and 0<=cstart<cols:
                    print(n[rstart][cstart])
                    tc+=1
            d+=1
        elif d==4:
            # up
            for i in range(steps):
                rstart-=1
                if 0<=rstart<rows and 0<=cstart<cols:
                    print(n[rstart][cstart])
                    tc+=1
            d=1

        # print('Steps = '+str(steps))
        # incrementing steps after every 2 directions
        direction_change+=1
        if direction_change%2==0:
            steps+=1


n = [[1,2,3],[4,5,6],[7,8,9]]
# n = [[1,2,3,11],[4,5,6,12],[7,8,9,13],[10,14,15,16]]
# n = [
#     [1,  2,  3,  4,  5],
#     [6,  7,  8,  9, 10],
#     [11,12,13,14,15]
# ]
rows=3
cols=3
rstart=1
cstart=1

traversal(n)
print('---------------------------------')
spiral_3_traversal(n,rows,cols,cstart,rstart)
print('---------------------------------')


