class Solution:
    def merge(self, num1: List[int], m: int, num2: List[int], n: int) -> None:
        
        ans=num1[:m]+num2[:n]
        ans.sort()
        num1[::]=ans[::]
        
        
        
        
        
        
        # """
        # Do not return anything, modify nums1 in-place instead.
        # """
        # i,j,k=0,0,0
        # res=[0*(len(num1)+len(num2))]
        # while(i<m and j<n):
        #     if(num2[j]<=num1[i]):
        #         res[k]=num2[j]
        #         j+=1
        #     else:
        #         res[k]=num1[i]
        #         i+=1
        #     k+=1
        # while(i<m):
        #     res[k]=num1[i]
        #     i+=1
        #     k+=1
        # while(j<n):
        #     res[k]=nums2[j]
        #     j+=1
        #     k+=1
        # num1[::]=res[::]