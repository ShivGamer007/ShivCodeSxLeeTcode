class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: return 0
        cnt = Counter(s)
        
        f = 0
        for i in cnt.values():
            if i < k:
                f = 1
        
        if len(cnt) < 3 or f:
            return -1
        
        cnt_ex = defaultdict(int)
        ans, l = 0, 0
        
        for r, ch in enumerate(s):
            cnt_ex[ch] += 1
            while cnt[ch] - cnt_ex[ch] < k:
                cnt_ex[s[l]] -= 1
                l += 1
            ans = max(r-l+1, ans)
        
        return len(s)-ans
        
        
        
        