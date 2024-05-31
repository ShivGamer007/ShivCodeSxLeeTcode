class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = nums[0]
        for i in range(1, len(nums)):
            x ^= nums[i]

        right_most = (x & (x-1)) ^ x

        b1, b2 = 0, 0
        for i in range(len(nums)):
            if nums[i] & right_most:
                b1 = b1 ^ nums[i]
            else:
                b2 = b2 ^ nums[i]

        return [b1, b2]
    
