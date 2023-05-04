class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        snt=list(senate)
        rq,dq=deque(),deque()
        
        for i,x in enumerate(snt):
            if x=="R":
                rq.append(i)
            else:
                dq.append(i)
        while rq and dq:
            r=rq.popleft()
            d=dq.popleft()
            if r<d:
                rq.append(d+len(snt))
            else:
                dq.append(r+len(snt))
        
        return "Radiant" if rq else "Dire"