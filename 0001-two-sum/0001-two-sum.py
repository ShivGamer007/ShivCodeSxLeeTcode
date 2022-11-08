class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        ans=[]
        for i in range(n):
            if target-nums[i] in nums[:i]:
                ans.append(i)
                ans.append(nums.index(target-nums[i]))
        return ans
            
            
            
        # ans=[]
        # n=len(nums)
        # for i in range(n):
        #     for j in range(n-1,-1,-1):
        #         if nums[i]+nums[j]==target:
        #             ans.append(i)
        #             ans.append(j)
        #             break
        # return list(set(ans))