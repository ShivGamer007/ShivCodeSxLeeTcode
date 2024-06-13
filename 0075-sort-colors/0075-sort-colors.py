class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z, o, t = 0, 0, len(nums)-1
        while o <= t:
            if nums[o] == 0:
                nums[o], nums[z] = nums[z], nums[o]
                o += 1
                z += 1
            elif nums[o] == 1:
                o += 1
            else:
                nums[o], nums[t] = nums[t], nums[o]
                t -= 1