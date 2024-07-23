from collections import defaultdict
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        mp = defaultdict(int)
        for i in range(len(nums)):
            mp[nums[i]] += 1
        mp = sorted(mp.items(), key = lambda x: x[1])
        x = []
        for k,v in mp:
            while v != 0:
                # print(k, v)
                x.append(k)
                v -= 1
        return x
            