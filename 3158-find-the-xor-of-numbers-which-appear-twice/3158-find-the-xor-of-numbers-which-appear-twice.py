class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ans = 0
        mp = {}
        twice = []
        for i in range(len(nums)):
            mp[nums[i]] = mp.get(nums[i], 0)+1
        for i in mp:
            if mp[i] == 2:
                twice.append(i)
        for i in twice:
            ans ^= i
        return ans