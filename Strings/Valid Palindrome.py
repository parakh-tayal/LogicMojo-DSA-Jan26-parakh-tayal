
def ispalindrome_using_extra_space(s):
    new=[]
    for i in s:
        #only picking alphabets
        if (ord(i)>=97 and ord(i)<=122):
            new.append(i)
        # if uppercase, converting to lowercase then
        elif (ord(i)>=65 and ord(i)<=90):
            new.append(chr(ord(i)+32))

    # print(''.join(new[::]))
    # print(''.join(new[::-1]))
    l=0
    r=len(new)-1
    while l<r:
        if new[l]!=new[r]:
            return False
        l+=1
        r-=1
    return True

def ispalindrome(s):
    # without using extra space
    l=0
    r=len(s)-1
    while l<=r:
        if (ord(s[l])>=97 and ord(s[l])<=122) or (ord(s[l])>=65 and ord(s[l])<=90) or (48 <= ord(s[l]) <= 57) :
            pass
        else:
            l+=1
            continue
        if (ord(s[r])>=97 and ord(s[r])<=122) or (ord(s[r])>=65 and ord(s[r])<=90) or (48 <= ord(s[r]) <= 57) :
            pass
        else:
            r-=1
            continue

        if (ord(s[l])>=65 and ord(s[l])<=90):
            x=chr(ord(s[l])+32)
        else:
            x=s[l]
        if (ord(s[r])>=65 and ord(s[r])<=90):
            y=chr(ord(s[r])+32)
        else:
            y=s[r]

        if x!=y:
            return False
            
        l+=1
        r-=1
    return True

# s = "A man, a plan, a canal: Panama"
s = "0P"
print(ispalindrome_using_extra_space(s))
print(ispalindrome(s))
