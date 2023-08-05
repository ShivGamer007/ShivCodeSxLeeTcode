#User function Template for python3

class Solution:

    def findMinDiff(self, arr, n, m):
        # code here
        arr.sort()
        i = 0
        j = m-1
        ans = float('inf')
        while j<n:
            if arr[j]-arr[i]<ans:
                ans = arr[j]-arr[i]
            i+=1
            j+=1
        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends