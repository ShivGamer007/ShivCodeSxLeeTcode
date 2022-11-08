class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in s:
            if stack and stack[-1]==i.swapcase():
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
#         s=list(st)
#         if len(s)<=1:
#             return s
#         for i in range(len(s)-1):
#             if ord(s[i])==ord(s[i+1])+32 or ord(s[i+1])==ord(s[i])+32:
#                 s[i]=" "
#                 s[i+1]=" "
#         ans=[]
#         for i in range(len(s)):
#             if s[i]!=" ":
#                 ans.append(s[i])
                
#         return ''.join(ans)
                