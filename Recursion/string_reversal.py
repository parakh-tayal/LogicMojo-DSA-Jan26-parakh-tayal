def string_reversal(s,i=0):
    if i+1==len(s):
        return s[i]
    return string_reversal(s,i+1) + s[i]
    
s='parakh'
print(string_reversal(s))