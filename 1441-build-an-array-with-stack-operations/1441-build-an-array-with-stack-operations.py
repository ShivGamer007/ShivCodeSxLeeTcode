class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        st = set(target)
        res = []
        for i in range(1, target[-1]+1):
            if i in st:
                res.append("Push")
            else:
                res.append("Push")
                res.append("Pop")
        return res