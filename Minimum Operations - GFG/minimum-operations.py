#User function Template for python3

class Solution:
    def minOperation(self, n):
        # code here 
        op = 0
        while n:
            if n%2 == 0:
                n //= 2
            else:
                n -= 1
            op += 1
        return op


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.minOperation(n))
# } Driver Code Ends