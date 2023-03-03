class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h=len(haystack)
        n=len(needle)
        if n==0: return 0
        x=[0]*n
        j=0
        for i in range(1,n):
            while j>0 and needle[j]!=needle[i]:
                j=x[j-1]
            if needle[j]==needle[i]:
                j+=1
            x[i]=j
        j=0
        for i in range(h):
            while j>0 and needle[j]!=haystack[i]:
                j=x[j-1]
            if needle[j]==haystack[i]:
                j+=1
            if j==n:
                return i-n+1
        return -1
                        
       