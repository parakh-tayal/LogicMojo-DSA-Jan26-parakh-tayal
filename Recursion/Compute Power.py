def powers(a,b):
    if b==1:
        return a
    return a*powers(a,b-1
    )
    
a=5
b=3
print(powers(a,b))