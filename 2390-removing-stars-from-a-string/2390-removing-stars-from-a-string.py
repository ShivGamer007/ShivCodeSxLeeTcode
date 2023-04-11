class Solution:
    def removeStars(self, s: str) -> str:
        c=0
        ans=""
        for i in range(len(s)-1,-1,-1):
            if c==0 and s[i]!='*':
                ans+=s[i]
            else:
                if s[i]=='*':
                    c+=1
                else:
                    c-=1
        l=[i for i in ans]
        l.reverse()
        ans="".join(l)
        return ans