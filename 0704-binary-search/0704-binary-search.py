class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            return 0 if nums[0]==target else -1
        l,r=0,len(nums)-1
        while(l<=r):
            mid=l+(r-l)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                r=mid-1
            else:
                l=mid+1
        return -1