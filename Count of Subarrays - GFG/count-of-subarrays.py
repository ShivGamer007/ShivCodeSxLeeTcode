#User function Template for python3
class Solution:
	def countSubarray(self,arr, n, k):
	    # code here
        s = 0
        i = 0
        while (i < n):
            if (arr[i] > k):
             
                i = i + 1
                continue
            count = 0
            while (i < n and arr[i] <= k):
                i = i + 1
                count = count + 1
            s = s + ((count*(count + 1))//2)
        
        return (n*(n + 1)//2 - s)

#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n, k=map(int, input().strip().split())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.countSubarray(arr, n, k)
        print(ans)
        tc=tc-1
# } Driver Code Ends