class Solution(object):
    def create_longest_palindrome_length(self, n):
        """
        :type s: str
        :rtype: bool
        """
        hash = {}
        for i in n:
            hash[i] = hash.get(i,0)+1
        
        length=0
        for i in hash.values():
            length+= (i//2) * 2

        if length < len(n):
            length+=1
        
        return length

    def create_longest_palindrome_string(self, n):
        hash = {}
        for i in n:
            hash[i] = hash.get(i,0)+1
        
        arr=[0]*len(n)
        l=length=0
        r=len(n)-1
        odd_char=''

        for i,j in hash.items():
            res = (j//2)*2
            res_count=0
            while l<r and res_count<res:
                arr[l]=arr[r]=i
                l+=1
                r-=1
                res_count+=2
            length+=1
            if j%2==1:
                odd_char=i

        if len(odd_char)>0:
            arr[l]=odd_char
        
        s=''
        for i in arr:
            if i!=0:
                s+=i
        return s

        
obj = Solution()
s = "abccccdd"
print(s)
print(obj.create_longest_palindrome_length(s))
print(obj.create_longest_palindrome_string(s))

# If you want, next I can show you a very powerful realization about palindromes that helps solve 5 different LeetCode problems instantly once you see it.