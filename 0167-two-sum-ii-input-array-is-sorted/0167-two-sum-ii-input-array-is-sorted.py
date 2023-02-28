class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        for i in range(len(nums)):
            if (target-nums[i]) in mp:
                if mp[target-nums[i]]!=i:
                    return [mp[target-nums[i]]+1,i+1]
            mp[nums[i]]=i
        return