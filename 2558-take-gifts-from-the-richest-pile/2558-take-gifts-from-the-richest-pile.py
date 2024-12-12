class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        for i in range(k):
            mx = max(gifts)
            gifts[gifts.index(mx)] = int((mx)**0.5)
        return sum(gifts)