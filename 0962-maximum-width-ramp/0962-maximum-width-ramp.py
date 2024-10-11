class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stk = []
        ans = 0
        for i in range(len(nums)):
            if not stk or nums[i] < nums[stk[-1]]:
                stk.append(i)
                
        for j in range(len(nums)-1, -1, -1):
            while stk and nums[j] >= nums[stk[-1]]:
                x = stk.pop()
                ans = max(ans, j-x)
        return ans