class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
    def bf(self,s,k):
        vowels=['a','e','i','o','u']
        max_count=float('-inf')
        for i in range(len(s)-k+1):
            count=0
            for j in range(i,i+k):
                if s[j] in vowels:
                    count+=1
            max_count=max(max_count,count)
        return max_count
    
    def slidingwindow_fixed(self,s,k):
        vowels=['a','e','i','o','u']
        max_count=float('-inf')
        l=0
        r=0
        res=0
        while r<len(s):
            if s[r] in vowels:
                res+=1
            if r-l+1==k:
                max_count=max(max_count,res)
                if s[l] in vowels:
                    res-=1
                #     print('l',s[l],s[r],res)
                # else:
                #     print('l',s[l],'not vowel - skipping')
                l+=1
            r+=1
        return max_count

obj = Solution()
s = "abciiidef"
k = 3
# s="aeiou"
# k=2
# s="leetcode"
# k=3

print(obj.bf(s, k))
print(obj.slidingwindow_fixed(s, k))

