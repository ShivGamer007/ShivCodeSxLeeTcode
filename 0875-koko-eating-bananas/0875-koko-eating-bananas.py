class Solution:
    def fun(self,piles,mid):
        x=0
        for i in piles:
            if(i%mid==0):
                x+=i//mid
            else:
                x+=(i//mid)+1
        return x
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while(l<=r):
            mid=l+(r-l)//2
            x=self.fun(piles,mid)
            if(x<=h):
                r=mid-1
            else:
                l=mid+1
        return l
