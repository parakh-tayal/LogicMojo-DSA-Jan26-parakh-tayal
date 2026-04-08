def move_x_to_end(s,i=0):
    if i==len(s)-1:
        return s[i]
    
    if s[i]=='x':
        return move_x_to_end(s,i+1)+'x'
    else:
        return s[i]+move_x_to_end(s,i+1)

    
    
s='pxaxraxkh'
print(move_x_to_end(s))


"""axbxcx

''+a
a+f+x=abcxx

b+f=bcx

c+f=c+x

x
"""
