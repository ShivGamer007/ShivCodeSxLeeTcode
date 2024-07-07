class Solution:
    def numWaterBottles(self, bottle: int, ex: int) -> int:
        if bottle < ex:
            return bottle
        ans = bottle
        empty = bottle
        
        while empty >= ex:
            nw = empty//ex
            ans += nw
            empty = nw + (empty % ex)
        
        return ans