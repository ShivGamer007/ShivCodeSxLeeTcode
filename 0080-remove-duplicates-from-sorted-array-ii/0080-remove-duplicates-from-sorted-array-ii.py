class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        c = 1
         
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                c += 1
            else:
                c = 1
            
            if c <= 2:
                nums[k] = nums[i]
                k += 1
        return k