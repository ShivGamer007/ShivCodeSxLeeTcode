class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[False]*len(candies)
        mx=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=mx:
                ans[i]=True
        return ans