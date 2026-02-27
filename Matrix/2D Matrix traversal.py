n = [[1,2,3],[4,5,6],[7,8,9]]

for rows in range(len(n)):
    for cols in range(len(n[0])):
        print(n[rows][cols],end=' ')
    print('\n')