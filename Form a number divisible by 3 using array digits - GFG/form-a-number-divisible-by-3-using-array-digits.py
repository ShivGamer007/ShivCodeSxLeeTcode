#User function Template for python3

class Solution:
    def isPossible(self, N, arr):
        # code here
        # x = arr[0]
        # for i in range(1, N):
        #     x *= 10*(len(str(arr[i])))
        #     x += arr[i]
        
        sm = sum(arr)
        # for i in arr:
        #     sm += i
        if sm % 3 == 0:
            return 1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.isPossible(N, arr))
# } Driver Code Ends