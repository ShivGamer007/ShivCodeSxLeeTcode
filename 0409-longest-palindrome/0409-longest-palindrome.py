from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        mp = Counter(s)
        # print(mp)
        x = list(mp.values())
        odd = []
        for i in x:
            if i%2:
                ans += (i-1)
                odd.append(i)
            else:
                ans += i
        return ans + 1 if len(odd)>0 else ans
        