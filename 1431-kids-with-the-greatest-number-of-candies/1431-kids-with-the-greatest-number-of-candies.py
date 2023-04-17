class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[False]*len(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=max(candies):
                ans[i]=True
        return ans