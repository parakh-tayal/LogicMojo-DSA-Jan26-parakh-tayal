# def longest_subarray_sum_0(n):
#     curr_sum={0:-1}
#     res=0
#     longest_sub=0
#     for i in range(len(n)):
#         res+=n[i]
#         if res in curr_sum:
#             ans=i-curr_sum[res]
#             longest_sub=max(longest_sub,ans)
#         else:
#             curr_sum[res]=i
#     return longest_sub

def longest_subarray_sum_0(n):
    hash={0:-1}
    res=0
    longest_sub=0
    for i in range(len(n)):
        res+=n[i]
        if res in hash:
            longest_sub=max(longest_sub,i-hash[res])
        else:
            hash[res]=i
    return longest_sub

n=[5,3,-1,-3,1]
print(longest_subarray_sum_0(n))