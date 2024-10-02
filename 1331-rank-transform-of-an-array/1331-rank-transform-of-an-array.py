from collections import defaultdict
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        x = sorted(list(set(arr)))
        mp = defaultdict(int)
        for rank, val in enumerate(x):
            mp[val] = rank+1
        for i in range(len(arr)):
            arr[i] = mp[arr[i]]
        return arr