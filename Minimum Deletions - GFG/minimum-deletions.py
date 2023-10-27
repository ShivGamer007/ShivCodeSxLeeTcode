#User function Template for python3

class solution:
    def minimumNumberOfDeletions(self,s):
        # code here 
        n=len(s)
        dp=[[None] * (n+1) for i in range(n+1)]
        
        for i in range(n + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s[i-1] == s[-j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        ans = (n-dp[n][n])     
        return ans



#{ 
 # Driver Code starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        s=input()

        ob = solution()
        print(ob.minimumNumberOfDeletions(s))
# } Driver Code Ends