class Solution:
    def arrangeCoins(self, n: int) -> int:
        #binary search
        l=1
        r=n
        while(l<=r):
            mid=l+(r-l)//2
            k=(mid*(mid+1))//2
            if k==n:
                return mid
            if k<n:
                l=mid+1
            else:
                r=mid-1
        return r