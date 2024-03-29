class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        time = [0, 0, 0]
        dc = {0: 'M', 1: 'P', 2: 'G'}
        for i in range(len(garbage) - 1, -1 , -1):
            for j in range(3):
                time[j] += garbage[i].count(dc[j])
                if (i != 0) and (time[j] != 0):
                    time[j] += travel[i-1]
        ans = sum(time)
        return ans