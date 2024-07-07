class Solution:
    def numWaterBottles(self, bottle: int, ex: int) -> int:
        
        extra = (bottle-1) // (ex-1) # cause you get one full bottle for every (ex-1) empty bottles
        return bottle + extra
    
#         if bottle < ex:
#             return bottle
#         ans = bottle
#         empty = bottle
        
#         while empty >= ex:
#             nw = empty//ex
#             ans += nw
#             empty = nw + (empty % ex)
        
#         return ans