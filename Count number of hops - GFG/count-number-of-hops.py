#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    # def __init__(self):
    #     self.mod = 1000000007
    def countWays(self,n):
        # code here
        if n==1 or n==2: return n
        if n==3: return 4
        mod = 1000000007
        dp = [0]*(n+1)
        dp[0],dp[1],dp[2],dp[3] = 0,1,2,4
        for i in range(4,n+1):
            dp[i] = (dp[i-1]%mod+dp[i-2]%mod+dp[i-3]%mod)%mod
        return dp[n]        
        
        
        
        
        # if (n==1 or n==2):
        #     return n
        # if n==3:
        #     return 4
        # return self.countWays(n-1)%self.mod+self.countWays(n-2)%self.mod+self.countWays(n-3)%self.mod


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
# } Driver Code Ends