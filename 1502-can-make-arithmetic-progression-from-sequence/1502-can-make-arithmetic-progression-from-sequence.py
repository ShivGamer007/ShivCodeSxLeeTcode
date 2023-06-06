class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) <= 2: return True
        arr.sort()
        dif = arr[1]-arr[0]
        for i in range(2,len(arr)):
            if dif != arr[i] - arr[i-1]:
                return False
        return True