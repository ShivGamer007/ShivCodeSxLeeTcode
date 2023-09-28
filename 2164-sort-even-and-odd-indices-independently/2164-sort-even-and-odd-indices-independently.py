class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even,odd = [],[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        
        even.sort()
        odd.sort(reverse = True)
        
        x = 0
        i,j = 0,0
        res = []
        while(x<len(nums)):
            if x%2==0:
                res.append(even[i])
                i += 1
            else:
                res.append(odd[j])
                j += 1
            x += 1
        return res