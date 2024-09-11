class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x, y = bin(start)[2:], bin(goal)[2:]
        if start < goal:
            while len(x) != len(y):
                x = "0" + x
        else:
            while len(x) != len(y):
                y = "0" + y
        c = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                c += 1
        return c