from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = Counter(arr1)
        x = []
        for i in arr1:
            if i not in arr2:
                x.append(i)
        ans = []
        for i in arr2:
            ans.extend([i]*mp[i])
        # print(x)
        ans.extend(sorted(x))
        return ans