class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q=stones[::]
        q.sort(reverse=True)
        while(len(q)>1):
            a=q[0]
            q.pop(0)
            b=q[0]
            q.pop(0)
            if(a!=b):
                q.append(abs(a-b))
            q.sort(reverse=True)
        return 0 if len(q)==0 else q[0]
        