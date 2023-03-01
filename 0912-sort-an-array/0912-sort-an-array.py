class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)//2,-1,-1):
            self.maxheapify(nums,i,len(nums))
        for i in range(len(nums)-1,0,-1):
            nums[0],nums[i]=nums[i],nums[0]
            self.maxheapify(nums,0,i)
        return nums
    def maxheapify(self, nums,i,n):
        l=2*i+1
        r=2*i+2
        largest=i
        if l<n and nums[l]>nums[largest]:
            largest=l
        if r<n and nums[r]>nums[largest]:
            largest=r
        if largest != i:
            nums[i],nums[largest]=nums[largest],nums[i]
            self.maxheapify(nums,largest,n)
        
        
        
        
        
  