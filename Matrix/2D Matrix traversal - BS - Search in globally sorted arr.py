"""
 Search a element in 2D sorted Matrix
"""
def bs(nums,target):
    l=0
    r=len(nums)
    while l<r:
        mid=int((l+r)//2)
        if nums[mid]<target:
            l=mid+1
        else:
            r=mid
    if l==len(nums) or nums[l]!=target:
        return -1
    return l


def bs_row_wise(n,target):
    rows=len(n)
    cols=len(n[0])
    for i in range(rows):
        if bs(n[i],target):
            return True
            # return [i,bs(n[i],target)]
    return False

def bs_row_wise_optimized(n,target):
    rows=len(n)
    cols=len(n[0])
    for i in range(rows):
        if target<=n[i][cols-1]:
            col_index=bs(n[i],target)
            if col_index!=-1:
                # return [i,col_index]
                return True
    return False



n = [[1,2,3],[4,5,6],[7,8,9]]
target=9
print(n)
print('---------------------------------')
# print(bs_row_wise(n,target))
print('---------------------------------')
print(bs_row_wise_optimized(n,target))
