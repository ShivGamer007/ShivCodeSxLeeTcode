class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk=[]
        i=0
        for n in pushed:
            stk.append(n)
            while len(stk)>0 and stk[len(stk)-1]==popped[i]:
                stk.pop()
                i+=1
        return True if len(stk)==0 else False