class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        while len(piles)>0:
            piles.pop(0)
            piles.pop()
            ans += piles[-1]
            piles.pop()
        return ans
        
        
        
        # piles.sort()
        # q = collections.deque(piles)
        # ans = 0
        # while len(q) > 0:
        #     q.popleft()
        #     q.pop()
        #     ans += q[-1]
        #     q.pop()
        # return ans
