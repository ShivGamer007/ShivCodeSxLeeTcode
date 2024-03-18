class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        last=points[0][1]
        ans=1
        for i in points:
            if i[0]>last:
                ans+=1
                last=i[1]
            last=min(i[1],last)
        return ans

