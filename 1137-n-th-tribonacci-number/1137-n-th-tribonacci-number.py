class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        l=[]
        l.append(0)
        l.append(1)
        l.append(1)
        for i in range(3,n+1):
            l.append(l[i-1]+l[i-2]+l[i-3])
        return l[n];