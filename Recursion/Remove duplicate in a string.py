def remove_duplicate_string(s,hash=set(),i=0):
    if i==len(s):
        return ''
    elif s[i] in hash:
        return remove_duplicate_string(s,hash,i+1)
    else:
        hash.add(s[i])
        return s[i] + remove_duplicate_string(s,hash,i+1)

s='parakh'
print(remove_duplicate_string(s))





