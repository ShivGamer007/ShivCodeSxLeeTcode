class Solution:
    def minCost(self, clr: str, neededTime: List[int]) -> int:
        sm = 0
        cur = clr[0]
        mx = neededTime[0]
        for i in range(1, len(neededTime)):
            if cur == clr[i]:
                if neededTime[i] > mx:
                    sm += mx
                    mx = neededTime[i]
                else:
                    sm += neededTime[i]
            else:
                cur = clr[i]
                mx = neededTime[i]
        return sm
   