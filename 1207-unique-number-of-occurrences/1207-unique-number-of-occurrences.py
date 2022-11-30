from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dc=list(Counter(arr).values())
        if len(set(dc))!=len(dc):
            return False
        # # print (dc)
        # for i in range(len(dc)):
        #     # print(dc[:i]+dc[i+1:])
        #     if i+1<len(dc):
        #         if dc[i] in dc[:i]+dc[i+1:]:
        #             return False
        #     else:
        #         if dc[i] in dc[:i-1]:
        #             return False
        return True