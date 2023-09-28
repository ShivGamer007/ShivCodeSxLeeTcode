class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even+odd
         
        # for i in range(len(nums)):
        #     if nums[i] % 2 == 0:
        #         x = nums[i]
        #         nums.remove(x)
        #         nums.insert(0, x)
        # return nums