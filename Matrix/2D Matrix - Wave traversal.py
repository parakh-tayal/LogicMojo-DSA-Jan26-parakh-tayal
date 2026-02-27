"""
 Wave traversal
"""
# def wave_traversal(n):
#     """
#     State driven like 
#     when r==0 start top to bottom
#     when r==len(n) start bottom to top
#     """
#     r=0
#     c=0
#     while c<len(n):
#         if r==0:
#             while r<len(n[0]):
#                 print(n[r][c],end=' ')
#                 r+=1
#         elif r==len(n[0]):
#             r-=1
#             while r>=0:
#                 print(n[r][c],end=' ')
#                 r-=1
#             r+=1
#         # print(r,c)
#         print('\n')
#         c+=1

def column_wave_traversal(n):
    """
    Using odd even
    if even then top to bottom
    if odd then bottom to top
    """
    r=0
    c=0
    while c<len(n[0]):
        if c%2==0:
            r=0
            while r<len(n):
                print(n[r][c],end=' ')
                r+=1
        else:
            r=len(n)-1
            while r>=0:
                print(n[r][c],end=' ')
                r-=1
        print('\n')
        c+=1

def row_wave_traversal(n):
    r=0
    c=0
    while r<len(n):
        if r%2==0:
            c=0
            while c<len(n[0]):
                print(n[r][c],end=' ')
                c+=1
        else:
            c=len(n[0])-1
            while c>=0:
                print(n[r][c],end=' ')
                c-=1
        print('\n')
        r+=1

n = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(n)
print('---------------------------------')
column_wave_traversal(n)
print('---------------------------------')
row_wave_traversal(n)


