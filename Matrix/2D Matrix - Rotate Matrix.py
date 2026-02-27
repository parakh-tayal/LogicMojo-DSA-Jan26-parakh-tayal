def traversal(n):
    for rows in range(len(n)):
        for cols in range(len(n[0])):
            print(n[rows][cols],end=' ')
        print('\n')

def transpose(n):
    for r in range(len(n)):
        for c in range(r,len(n[0])):
            n[r][c],n[c][r]=n[c][r],n[r][c]
    return n

def reverse_rows(n):
    for row in range(len(n)):
        l=0
        r=len(n)-1
        while l<r:
            n[row][l],n[row][r]=n[row][r],n[row][l]
            l+=1
            r-=1
    return n

def rotate_matrix(n):
    """
    1. Transpose the matrix
    2. Reverse the rows
    """
    n=transpose(n)
    n=reverse_rows(n)
    return n


n = [[1,2,3],[4,5,6],[7,8,9]]
# n = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
traversal(n)
print('-----')
print(rotate_matrix(n))
print('-----')



