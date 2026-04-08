"""
Ignore
- 0
- Negative nums
- nums > len(n)
- Duplicate

Approach:
1. Cyclic Sort/Array Indexing
 - keep sorting until all the values are at right place, so we're using WHILE LOOP here

Notes:
n[correct] != n[i] does

A. Avoid duplicate swap
B. Avoid infinite loop
"""

def firstMissingPositive(n):
    i=0
    while i<len(n):
        correct=n[i]-1
        if correct!=i and n[i]<=len(n) and n[i]>0 and n[i] != n[correct]:
            n[i],n[correct]=n[correct],n[i]
        else:
            i+=1

    for i in range(len(n)):
        if i!=n[i]-1:
            return i+1
    return len(n)+1

n = [3, 4, -1, 1,1]
print(firstMissingPositive(n))