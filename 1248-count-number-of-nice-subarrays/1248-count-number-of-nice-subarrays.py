from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # [1,1,2,1,1] == [1,1,0,1,1] 
        nums = [1 if i&1 else 0 for i in nums]
        prefix_sum = defaultdict(int)

        sum, cnt = 0, 0
        for i in range(len(nums)):
            sum += nums[i]
            if(sum == k):
                cnt += 1
            if prefix_sum[sum - k] != 0:
                cnt += prefix_sum[sum - k]
            prefix_sum[sum] += 1
            
        return cnt