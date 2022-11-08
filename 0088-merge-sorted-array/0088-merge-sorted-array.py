class Solution:
    def merge(self, num1: List[int], m: int, num2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans=num1[:m]+num2[:n]
        ans.sort()
        num1[::]=ans[::]
        