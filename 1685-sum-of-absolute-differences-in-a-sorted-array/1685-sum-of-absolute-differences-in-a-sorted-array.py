class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        total = 0
        
        for num in nums:
            total += abs(num-nums[0])
        ans.append(total)
        
        for i in range(1, n):
            tmp = nums[i] - nums[i-1]
            total += tmp*i
            total -= tmp*(n-i)
            ans.append(total)
            
        return ans        