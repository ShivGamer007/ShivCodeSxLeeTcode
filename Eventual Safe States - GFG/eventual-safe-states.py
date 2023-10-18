#User function Template for python3

from typing import List
from collections import defaultdict
class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        # code here
        ind_eg = [0]*(V)
        adj_r = defaultdict(list)
        
        for i in range(V):
            for it in adj[i]:
                adj_r[it].append(i)
                ind_eg[i]+=1
        
        q = []
        for i in range(V):
            if ind_eg[i]==0:
                q.append(i)
                
        ans = []
        while(q):
            node = q.pop(0)
            ans.append(node)
            for it in adj_r[node]:
                ind_eg[it]-=1
                if ind_eg[it]==0:
                    q.append(it)
        ans.sort()
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends