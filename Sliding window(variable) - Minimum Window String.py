from collections import deque

def minimum_window_string_my_version(n,t):
    hash={}
    for i in t:
        hash[i]=hash.get(i,0)

    l=0
    r=0
    mc=float('inf')
    arr={}
    q=deque()
    while r<len(n):
        flag_r=False
        if n[r] in hash and all(hash.values())==False:
            hash[n[r]]+=1
            q.append(r)
            flag_r=True
        elif n[l] in hash and all(hash.values()):
            if hash[n[l]]!=0:
                hash[n[l]]-=1
            # l+=1
            q.popleft()
            l=q[0]
        else:
            flag_r=True

        if all(hash.values()):
            # print(hash)
            # print(n[l:r+1])
            mc=min(mc,r-l+1)
            # if mc>(r-l+1):
            #     mc=(r-l+1)
            #     arr[n[l:r+1]]=(r-l+1)
        if flag_r==True:
            r+=1
        # print(l,r)
    return mc
    # return mc,arr

def minimum_window_string(n,t):
    hash_required={}
    for i in t:
        hash_required[i]=hash_required.get(i,0)+1

    hash_current={}
    mc=float('inf')
    q=deque()
    formed=0
    required=len(hash_required)
    l=0
    output=''
    for r in range(len(n)):
        char = n[r]
        if char in hash_required:
            hash_current[char]=hash_current.get(char,0)+1
            q.append(r)
            if hash_required[char]==hash_current[char]:
                formed+=1

        while formed==required:
            # recording minimum
            # mc=min(mc,r-l+1)
            l=q[0]   #giving l to correct boundary because we're recording first and updating l later. So this is for mainly recording FIRST CORRECT RECORDING 
            new_valid_length=r-l+1
            if mc>new_valid_length:
                mc=new_valid_length
                output=n[l:r+1]

            # shrinking left
            left_idx = q.popleft()
            left_char=n[left_idx]
            hash_current[left_char]-=1

            if hash_current[left_char]<hash_required[left_char]:
                formed-=1
            
            # jumping l to next valid char using q
            if q:
                l=q[0]
            else:
                l=left_idx+1
    if mc!=float('inf'):
        # return mc
        return output
    else: 
        return ''

n = 'ADOBECODEBANC'
t = 'ABC'
n="ab"
t='b'
print(minimum_window_string(n,t))