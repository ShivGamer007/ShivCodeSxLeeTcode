class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1=len(word1)
        n2=len(word2)
        ans=""
        i,j=0,0
        while(n1 or n2):
            if n1:
                ans+=word1[i]
                i+=1
                n1-=1
            if n2:
                ans+=word2[j]
                j+=1
                n2-=1
        return ans