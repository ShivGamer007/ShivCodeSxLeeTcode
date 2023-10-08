class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        dot_product = [[0] * 505 for _ in range(505)]
        n1, n2 = len(nums1), len(nums2)
        
        firstmx, secondmx = max(nums1), max(nums2)
        firstmn, secondmn = min(nums1), min(nums2)
        
        if (firstmx < 0 and secondmn > 0) or (firstmn > 0 and secondmx < 0):
            return max(firstmx * secondmn, firstmn * secondmx)
        
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                cur_dot = nums1[i]*nums2[j] + dot_product[i+1][j+1]
                dot_product[i][j] = max(cur_dot, dot_product[i][j+1], dot_product[i+1][j])
                
        return dot_product[0][0]