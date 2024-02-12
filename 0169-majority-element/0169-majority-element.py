class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frq, ans = 0, nums[0]
        cnt = Counter(nums)
        for i in cnt:
            if cnt[i]>frq:
                frq = cnt[i]
                ans = i
        return ans