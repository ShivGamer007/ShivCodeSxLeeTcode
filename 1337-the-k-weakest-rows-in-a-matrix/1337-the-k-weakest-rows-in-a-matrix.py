class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = []
        dc = {}
        for i in range(len(mat)):
            dc[i] = mat[i].count(1)
        # print(dc)
        tmp = list(dc.values())
        tmp.sort()
        # print(tmp)
        for i in range(k):
            for x in dc:
                if dc[x] == tmp[0]:
                    ans.append(x)
                    del dc[x]
                    break
                    
            tmp.pop(0)
                
        
        return ans