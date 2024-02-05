class Solution:
    def firstUniqChar(self, s: str) -> int:
        x = [i for i in s]
        dc = defaultdict(int)
        for i in x:
            dc[i] = dc.get(i, 0) + 1
        for i in range(len(x)):
            if dc[x[i]] == 1:
                return i
        return -1