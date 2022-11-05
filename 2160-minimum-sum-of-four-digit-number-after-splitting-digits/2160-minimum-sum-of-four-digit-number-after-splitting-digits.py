class Solution:
    def minimumSum(self, num: int) -> int:
        s=[]
        for i in range(4):
            r=num%10
            num=num//10
            s.append(r)
        s.sort()
        n1,n2=0,0
        n1=s[0]*10+s[2]
        n2=s[1]*10+s[3]
        return n1+n2