class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return rec1[0]<rec2[2] and rec2[0]<rec1[2] and rec1[1]<rec2[3]  and rec2[1]<rec1[3]
        
#         a1,b1,a2,b2=rec1[0],rec1[1],rec1[2],rec1[3]
#         p1,q1,p2,q2=rec2[0],rec2[1],rec2[2],rec2[3]
        
#         if ((p1>a1 and p1<a2) or (p2>a1 and p2<a2)) and ((q1>b1 and q1<b2)or(q2>b1 and q2<b2)):
#             return True
#         if ((a1>p1 and a1<p2) or (a2>p1 and a2<p2)) and ((b1>q1 and b1<q2) or (b2>q1 and b2<q2)):
#             return True
#         if ((p1>a1 and p1<a2) or (p2>a1 and p2<a2)) and (q1==b1 or q1==b2 or q2==b1 or q2==b2):
#             return True
#         if (p1==a1 or p1==a2 or p2==a1 or p2==a2) and ((q1>b1 and q1<b2)or(q2>b1 and q2<b2)):
#             return True
#         return False
    
    