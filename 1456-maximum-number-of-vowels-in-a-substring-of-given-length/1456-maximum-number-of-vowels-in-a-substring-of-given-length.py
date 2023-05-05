class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n=len(s)
        vowel=['a','e','i','o','u']
        l,c,ans=0,0,0
        r=0
        while r!=n:
            c+=1 if s[r] in vowel else 0
            if r-l+1 > k:
                c-=1 if s[l] in vowel else 0
                l+=1
            ans=max(ans,c)
            
            r+=1
        return ans