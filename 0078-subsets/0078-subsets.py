class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def solve(ip, op):
            if (len(ip) == 0):
                ans.append(op[:])
                return 
            op1, op2 = op[:], op[:]
            op2.append(ip[0])
            # ip.pop(0)
            # print(ip)
            solve(ip[1:], op1)
            solve(ip[1:], op2)
        
        
        # Chat GPT
        
        # def solve(ip, op):
        #     ans.append(op)
        #     for i in range(len(ip)):
        #         solve(ip[i+1:], op + [ip[i]])
            
        solve(nums, [])
        return ans