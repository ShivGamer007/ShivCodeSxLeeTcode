class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0#buy
        r=1#sell
        mx_prft=0
        while r<len(prices):
            cur_prft=prices[r]-prices[l]
            if prices[l]<prices[r]:
                mx_prft=max(cur_prft,mx_prft)
            else:
                l=r
            r+=1
        return mx_prft
