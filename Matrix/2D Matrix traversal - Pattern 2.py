n = [[1,2,3],[4,5,6],[7,8,9]]
# op = 1,4,7  2,5,8  3,6,9

for cols in range(len(n[0])):
    for rows in range(len(n)):
        print(n[rows][cols],end=' ')
    print('\n')