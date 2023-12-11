class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        t = len(arr)//4
        for i in range(len(arr)):
            if arr.count(arr[i])>t:
                return arr[i]
        return -1