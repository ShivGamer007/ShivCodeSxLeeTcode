class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        for i in range(len(nums)):
            if nums[i] != 0:
                temp.append(nums[i])
        k = len(temp)
        for i in range(len(nums)):
            if k!=0:
                nums[i] = temp[i]
                k -= 1
            else:
                nums[i] = 0
            