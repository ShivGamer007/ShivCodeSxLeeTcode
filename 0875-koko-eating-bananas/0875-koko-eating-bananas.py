class Solution:
    def minEatingSpeed(self, piles: List[int], hrs: int) -> int:
        l=1
        r=max(piles)
        while(l<=r):
            mid=(l+r)//2
            h=0
            for i in piles:
                h+=i//mid+(i%mid!=0)
            if h<=hrs:
                r=mid-1
            else:
                l=mid+1
        return l        