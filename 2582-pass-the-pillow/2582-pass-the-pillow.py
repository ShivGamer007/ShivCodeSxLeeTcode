class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_len = 2*n - 2
        pos = time % cycle_len
        
        if pos < n:
            return pos+1
        else:
            return 2*n - pos - 1
