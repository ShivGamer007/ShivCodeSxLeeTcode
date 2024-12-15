class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extra: int) -> float:
        # max heap
        n = len(classes)
        def profit(a, b):
            return (a+1)/(b+1) - (a/b)
        
        mxheap = []
        for a, b in classes:
            a, b = a*1.0, b*1.0
            mxheap.append((-profit(a, b), a, b))
        
        heapq.heapify(mxheap)
        
        for i in range(extra):
            diff, a, b = heapq.heappop(mxheap)
            heapq.heappush(mxheap, (-profit(a+1, b+1), a+1, b+1))
            
        ans = sum(a/b for diff, a, b in mxheap)/n
        return ans