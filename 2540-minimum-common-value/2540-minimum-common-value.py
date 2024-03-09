class Solution:
    def getCommon(self, a: List[int], b: List[int]) -> int:
        # mp = defaultdict(int)
        # for n in a:
        #     mp[n] += 1
        # for n in b:
        #     if mp[n] > 0:
        #         return n
        # return -1

        
        i, j = 0, 0
        com = []
        while i<len(a) and j<len(b):
            if a[i] == b[j]:
                com.append(a[i])
                i += 1
                j += 1
            elif a[i]<b[j]:
                i += 1
            else:
                j += 1
        if len(com):
            return min(com)
        return -1
        # return min(com) if min(com)!=None else -1