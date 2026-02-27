"""
 [[1,2,3],[4,5,6],[7,8,9]]
 op = 1,4,7  2,5,8  3,6,9

 Swap rows and columns
"""

def using_additional_space(n):
    # creating new list and appending
    new_n=[]
    rows = len(n)
    cols = len(n[0])
    for i in range(rows):
        temp=[]
        for j in range(cols):
            temp.append(n[j][i])
        new_n.append(temp)
    return new_n

    
def using_without_space(n):
    # swapping in place
    rows = len(n)
    cols = len(n[0])
    for i in range(rows):
        for j in range(i,rows):
            n[i][j],n[j][i]=n[j][i],n[i][j]
    return n


n = [[1,2,3],[4,5,6],[7,8,9]]
print(n)
print('---------------------------------')
print(using_additional_space(n))
print('---------------------------------')
print(using_without_space(n))
