class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref) <= 1:
            return pref
        tmp = pref[0]
        for i in range(1, len(pref)):
            x = pref[i]
            pref[i] ^= tmp
            tmp = x
        return pref
        