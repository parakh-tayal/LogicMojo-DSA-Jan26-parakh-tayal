from collections import deque

def firstNonRepeatingChars(characters):
    q = deque()
    freq = [0]*26

    for char in characters:
        freq[ord(char)-ord('a')]+=1

        q.append(char)
        
        while q and freq[ord(q[0])-ord('a')]>1:
            q.popleft()

        if q:
            print(q[0])
        else:
            print(-1)


s = 'aabc'
firstNonRepeatingChars(s)