def desc(n):
    if n==1:
        return n
    return n*desc(n-1)
    
n=5
print(desc(n))