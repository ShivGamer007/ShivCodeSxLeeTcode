class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk=[]
        for c in s:
            if stk and c==stk[-1]:
                stk.pop()
            else:
                stk.append(c)
        return ''.join(stk)