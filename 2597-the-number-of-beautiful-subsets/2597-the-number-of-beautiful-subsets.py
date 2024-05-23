class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        def recursion(idx, cnt):
            if idx == n:
                return 1
            total = 0
            total += recursion(idx+1, cnt)
            
            if cnt[nums[idx]-k] == 0 and cnt[nums[idx]+k] == 0:
                cnt[nums[idx]] += 1
                total += recursion(idx+1, cnt)
                cnt[nums[idx]] -= 1
            return total
        
        ans = recursion(0, collections.Counter())-1
        return ans
        
        
        
        
        
        
        
        
#         ans = []
        
#         def solve(ip, op):
#             if len(ip)==0:
#                 x = []
#                 for i in op:
#                     if abs(i+k) in op or abs(i-k) in op:
#                         continue
#                     else:
#                         x.append(i)
#                 if len(x) != 0 and x[:] not in ans:
#                     ans.append(x[:])
#                 return
#             op1, op2 = op[:], op[:]
#             op2.append(ip[0])
#             solve(ip[1:], op1)
#             solve(ip[1:], op2)
#         solve(nums, [])
#         print(ans)
#         return len(ans)