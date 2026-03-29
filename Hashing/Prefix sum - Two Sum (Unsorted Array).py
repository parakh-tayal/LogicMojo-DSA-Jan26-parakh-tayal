"""
Approach - target-element
"""

def two_sum_1(n,target): # Exact 1 solution
    hash={0:0}
    for i in range(len(n)):
        res=target-n[i]
        if res in hash:
            return [hash[res],i]
        else:
            hash[n[i]]=i

def two_sum_2(n,target): # Multiple solutions
    hash={}
    arr=[]
    for i in range(len(n)):
        res=target-n[i]
        if res in hash:
            arr.append([hash[res],i])
        hash[n[i]]=i
    return arr

n=[2,7,11,9,0]
target=9
print(two_sum_1(n,target))
print(two_sum_2(n,target))
# o/p - [[0, 1], [-1, 3], [3, 4]]