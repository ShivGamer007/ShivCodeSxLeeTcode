from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        ans = []
        for i in range(len(strs)):
            x = strs[i]
            strs[i] = "".join(sorted([i for i in x]))
            mp[strs[i]].append(x)
        for i in mp:
            ans.append(mp[i])
        return ans