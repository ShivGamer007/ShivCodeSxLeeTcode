class Solution:
    def addDigits(self, num: int) -> int:
        if num==0: return 0
        x=[]
        while (num):
            x.append(num%10)
            num=num//10
        ans=x[0]
        if len(x)==1:
            return int(ans)
        p=sum(x)
        return self.addDigits(p)
        