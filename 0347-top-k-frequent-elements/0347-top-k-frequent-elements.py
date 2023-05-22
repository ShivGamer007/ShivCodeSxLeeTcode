from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict(Counter(nums))
        count = dict(sorted(count.items(), key = lambda x: x[1], reverse = True))
        arr = list(count.keys())
        ans = []
        for i in range(k):
            ans.append(arr[i])
        return ans