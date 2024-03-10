class Solution:
    def intersection(self, a: List[int], b: List[int]) -> List[int]:
        i, j = 0, 0
        a.sort()
        b.sort()
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
        return list(set(com))