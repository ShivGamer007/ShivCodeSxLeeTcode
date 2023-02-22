class Solution:
    def fun(self, mid, d, w):
        n=len(w)
        total=0
        day=1
        isvalid=True
        for i in range(n):
            if w[i]>mid:
                isvalid=False
            if total+w[i]<=mid:
                total+=w[i]
            else:
                day+=1
                total=w[i]
        if(not isvalid):
            return False
        else:
            return (day<=d)
        
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=1
        r=500*50000
        while(l<r):
            mid=(l+r)//2
            if(self.fun(mid,days,weights)):
                r=mid
            else:
                l=mid+1
        return l
            
        