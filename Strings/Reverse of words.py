"""
# s = ' hello world'
o/p = 'world hello'

# s = 'the sky is blue'
o/p = 'blue is sky the'

NOTE: Remove trailing and leading spaces in the output
"""

def issalphanum(x):
    if (ord(x)>=97 and ord(x)<=122) or (ord(x)>=65 and ord(x)<=90) or (48 <= ord(x) <= 57):
        return True
    else:
        return False

def reverse_of_words(s):
    # two pointer approach
    i=j=len(s)-1
    x=''
    space_flag=0
    while i>=0:
        if issalphanum(s[i]):
            if space_flag==0:
                space_flag=1
                j=i+1
        else:
            # print(j,i)
            x+=s[i+1:j]+' '
            space_flag=0
        i-=1

    # append first word if exists
    if space_flag == 1:
        x += s[0:j]
        
    return x.strip()

s = ' hello world '
# s = 'the sky is blue'
print(reverse_of_words(s))