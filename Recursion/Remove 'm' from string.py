def remove_string(s,t):
    # time complexity is O(n2) because string is being copied here everytime
    if len(s)==0:
        return ''
    first_char=s[0]
    rest_char=s[1:]

    if first_char!=t:
        return first_char + remove_string(rest_char,t)
    else:
        return remove_string(rest_char,t)
    
def remove_string_2(s,t,i=0):
    # O(n) because we're using indexing here
    if len(s)==i:
        return ''
    curr_char=s[i]

    if curr_char!=t:
        return curr_char + remove_string_2(s,t,i+1)
    else:
        return remove_string_2(s,t,i+1)

s='ambmcm'
t='m'
print(remove_string(s,t))
print(remove_string_2(s,t))


"""Lecture: March 15
max of array
string reversal
Move all x to end
palindrome check
remove duplicate in a string
"""