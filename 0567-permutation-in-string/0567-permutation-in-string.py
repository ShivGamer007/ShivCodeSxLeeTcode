class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt,n=Counter(s1),len(s1)
        for i in range(len(s2)):
            if s2[i] in cnt:
                cnt[s2[i]]-=1
            if i>=n and s2[i-n] in cnt:
                cnt[s2[i-n]]+=1
            if all([cnt[i]==0 for i in cnt]):
                return True
        return False
        
        
    