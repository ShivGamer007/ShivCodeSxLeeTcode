class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        x=0
        for i in num:
            x=x*10+i
        ans=x+k
        res=[]
        while(ans):
            r=ans%10
            res.append(r)
            ans=ans//10
        res=res[::-1]
        return res