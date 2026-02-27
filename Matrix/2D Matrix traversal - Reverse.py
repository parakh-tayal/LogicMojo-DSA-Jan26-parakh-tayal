

def reverse_row(n):
    # Reverse row op = 3,2,1 6,5,4 9,8,7
    rows=len(n)
    cols=len(n[0])
    for i in range(rows):
        for j in range(cols-1,-1,-1):
            print(n[i][j],end=' ')
        print('\n')
    
def reverse_col(n):
    # Reverse col op = 7,4,1 8,5,2 9,6,3
    rows=len(n)
    cols=len(n[0])
    for j in range(cols):
        for i in range(rows-1,-1,-1):
            print(n[i][j],end=' ')
        print('\n')


n = [[1,2,3],[4,5,6],[7,8,9]]
reverse_row(n)
print('-----')
reverse_col(n)



