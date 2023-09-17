#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        ans = [1,1,2]
        if n<=3:
            return ans[:n]
        
        for i in range(3,n):
            ans.append(ans[i-1]+ans[i-2])
        return ans
            
        
        
        
        
        
        
        # def fib(n):
        #     if n==0 or n==1:
        #         return n
        #     if n==2:
        #         return 1
        #     return fib(n-1)+fib(n-2)
            
        # ans = []
        # for i in range(1,n+1):
        #     ans.append(fib(i))
        # return ans
            
        # your code here
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends