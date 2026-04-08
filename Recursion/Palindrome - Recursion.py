def palindrome_check(s,l,r):
    if l>=r:
        return True
    elif s[l]!=s[r]:
        return False
    else:
        return palindrome_check(s,l+1,r-1)

s='abcba'
print(palindrome_check(s,l=0,r=len(s)-1))