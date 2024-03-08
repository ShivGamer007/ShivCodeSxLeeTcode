class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        mxfrq = max(cnt.values())
        ans = 0
        for i in cnt:
            if cnt[i] == mxfrq:
                ans += cnt[i]
        return ans