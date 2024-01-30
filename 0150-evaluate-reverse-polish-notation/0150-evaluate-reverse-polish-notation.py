class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op={
            "*":lambda x,y: x*y, "+": lambda x,y: x+y,
            "-":lambda x,y: x-y, "/": lambda x,y: x/y
        }
        stack=[]
        for i in tokens:
            if i not in op:
                stack.append(int(i))
            else:
                r=stack.pop()
                l=stack.pop()
                ans=op[i](l,r)
                stack.append(int(ans))
        return stack.pop()



