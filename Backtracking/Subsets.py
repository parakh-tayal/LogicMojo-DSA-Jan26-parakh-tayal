def subsets(nums):
    results=[]
    path=[]
    n=len(nums)

    def bt(curr=0):
        results.append(path[:])
        for i in range(curr,n):
            path.append(nums[i])
            bt(i+1)
            path.pop()
    
    bt()
    return results

nums=[1,2,3]
print(subsets(nums))