"""
 Search a element in 2D NOT GLOBALLY sorted Matrix
"""
def staircase_approach(n,target):
    r=0
    c=len(n[0])-1
    while r<len(n) and c>=0:
        if n[r][c]==target:
            return [r,c]
        elif n[r][c]>target:
            c-=1
        else:
            r+=1
    return -1

n = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target=26
print(n)
print('---------------------------------')
print(staircase_approach(n,target))
print('---------------------------------')
