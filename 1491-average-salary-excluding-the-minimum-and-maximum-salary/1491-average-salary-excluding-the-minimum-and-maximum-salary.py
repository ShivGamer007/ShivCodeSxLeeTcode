class Solution:
    def average(self, salary: List[int]) -> float:
        mx=max(salary)
        mn=min(salary)
        sm,c=0,0
        
        for i in salary:
            if i==mx or i==mn:
                continue
            else:
                sm+=i
                c+=1
        return sm/c
                
            