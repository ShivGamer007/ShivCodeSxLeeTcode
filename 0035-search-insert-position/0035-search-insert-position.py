class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target<nums[0]:
            return 0
        if target>nums[len(nums)-1]:
            return len(nums)
        l=0
        r=len(nums)-1
        while(l<=r):
            mid=l+(r-l)//2
            if nums[mid]==target or (nums[mid-1]<target and nums[mid]>target) :
                return mid
            
            if nums[mid]<target:
                l=mid+1
                continue
            else:
                r=mid-1
                continue