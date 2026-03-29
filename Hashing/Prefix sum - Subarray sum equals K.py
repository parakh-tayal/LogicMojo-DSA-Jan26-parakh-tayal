def subarray_sum_k(n,k):
    hash={0:-1}
    res=0
    count=0
    for i in range(len(n)):
        res+=n[i]
        if res-k in hash:
            count+=1
        hash[res] = hash.get(res,0)+1
    return count

n=[1,2,3]
k=3
print(subarray_sum_k(n,k))