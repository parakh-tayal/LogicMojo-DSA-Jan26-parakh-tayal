def desc(n):
    if n==0:
        return n
    desc(n-1)
    print(n)
    
n=5
desc(n)