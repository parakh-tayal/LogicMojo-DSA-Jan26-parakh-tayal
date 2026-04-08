def binary_search_recursion(n,target,l,r):
    if l>r:
        return -1

    mid=int((l+r)//2)
    if target<n[mid]:
        return binary_search_recursion(n,target,l,mid-1)
    elif n[mid]<target:
        return binary_search_recursion(n,target,mid+1,r)
    else:
        return mid
    
n=[1,2,4,5,6,7,8,9]
target=8
print(binary_search_recursion(n,target,l=0,r=len(n)-1))