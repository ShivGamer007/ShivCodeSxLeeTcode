class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []
        n = len(code)
        
        if k>0:
            x = sum(code[:k])
            for i in range(n):
                x = x-code[i]+code[(k+i)%n]
                ans.append(x)
        elif k<0:
            x = sum(code[k:])
            for i in range(n):
                ans.append(x)
                x = x+code[i]-code[(k+i)%n]
        else:
            for i in range(n):
                ans.append(0)
                
        return ans