def max_or_array(n,maxElement=float('-inf'),i=0):
    if not n:
        return -1
    
    maxElement=max(maxElement,n[i])
    if i+1==len(n):
        return maxElement
    else:
        return max_or_array(n,maxElement,i+1)
        
n=[1,2,3,4,5]
print(max_or_array(n))