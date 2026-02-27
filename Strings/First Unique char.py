
def first_unique_char(s):
    hash={}
    for i in s:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
    for i in range(len(s)):
        if s[i] in hash and hash[s[i]]==1:
            # return [i,True]
            return i
    return -1


# s = 'leetcode'
# s = 'loveleetcode'
s = 'aabb'
print(first_unique_char(s))