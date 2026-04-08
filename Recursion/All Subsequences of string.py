def subsequences_of_string(s,hash,new='',i=0):
    if i==len(s):
        hash.add(new)
        return hash
    subsequences_of_string(s,hash,new+s[i],i+1)     #include
    subsequences_of_string(s,hash,new,i+1)          #exclude
    return hash

s='abc'
hash=set()
print(subsequences_of_string(s,hash))





