#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		# Code here
		mp = {}
		for i in range(len(nums)):
		    mp[nums[i]] = mp.get(nums[i], 0)+1
		ans = []
		for i in mp:
		    if mp[i] == 1:
		        ans.append(i)
	    if ans[1]>ans[0]:
	        return ans[0], ans[1]
	    return ans[1], ans[0]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends