class Solution:
    
    def orderlyQueue(self, s: str, k: int) -> str:
        shivcodes=700*100
        return ''.join(sorted(list(s))) if k!=1 else min(s[i:]+s[:i] for i in range(len(s)))
            