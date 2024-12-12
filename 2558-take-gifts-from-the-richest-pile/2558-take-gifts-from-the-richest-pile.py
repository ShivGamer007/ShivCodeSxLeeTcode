class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
    #using heap (using -ve for converting minheap operations into maxheap operations)
    
        gifts = [-i for i in gifts]
        heapify(gifts)
        x = 2**32
        i = 0
        while i < k and x > 1:
            x = -heappop(gifts)
            heappush(gifts, -int(x**0.5))
            i += 1
            
        return -sum(gifts)
    
    
    # Brute Force
        # for i in range(k):
        #     mx = max(gifts)
        #     gifts[gifts.index(mx)] = int((mx)**0.5)
        # return sum(gifts)