class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        def help(i,v,l,temp):
            nonlocal ans
            if i==len(v):
                for t in temp:
                    if t!=0:
                        return
                ans = max(ans,l)
                return
            help(i+1,v,l,temp)
            temp[v[i][0]]-=1
            temp[v[i][1]]+=1
            help(i+1,v,l+1,temp)
            temp[v[i][0]]+=1
            temp[v[i][1]]-=1
        temp = [0]*n
        help(0,requests,0,temp)
        return ans
            