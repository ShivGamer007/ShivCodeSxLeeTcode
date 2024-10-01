class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        mod_frq = [0]*k
        
        for i in arr:
            rem = i % k
            
            mod_frq[rem] += 1
            
        if mod_frq[0] % 2 != 0:
            return False
        
        for i in range(1, (k//2)+1):
            if mod_frq[i] != mod_frq[k-i]:
                return False
            
        return True