from collections import defaultdict
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        mp = defaultdict(int)
        for i in roads:
            for j in i:
                mp[j] += 1
                
        smp = dict(sorted(mp.items(), key = lambda x: x[1], reverse = True))
        # print("smp = ", smp)
        arr = list(smp.keys())
        # print(arr)
        
        tmp = {}
        x = n
        for i in range(len(arr)):
            tmp[arr[i]] = x
            x -= 1
        # print("tmp = ",tmp)
        for road in roads:
            road[0], road[1] = tmp[road[0]], tmp[road[1]]
        
        ans = 0
        # print(roads)
        for i in roads:
            ans += sum(i)
        return ans