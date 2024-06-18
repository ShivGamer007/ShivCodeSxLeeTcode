from collections import defaultdict
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dif_pro = [[difficulty[i], profit[i]] for i in range(len(profit))]
        dif_pro.sort()
        worker.sort()
        ans = 0
        j = 0
        mx = 0
        for i in range(len(worker)):
            while j < len(dif_pro) and dif_pro[j][0] <= worker[i]:
                mx = max(mx, dif_pro[j][1])
                j += 1
            ans += mx
        return ans
        
        
        
        
        
        
        
        
        
        
#         def_pro = defaultdict(int)
#         for i in range(len(difficulty)):
#             def_pro[difficulty[i]] = profit[i]
      
#         difficulty.sort()
        
#         work_def = defaultdict(list) 
        
#         for i in range(len(worker)):
#             # x = []
#             l, r = 0, len(difficulty)-1
#             while l<r:
#                 mid = l+(r-l)//2
#                 if worker[i] >= difficulty[mid] and (difficulty[mid+1] and worker[i] < difficulty[mid+1]):
#                     break
#                 elif worker[i] < difficulty[mid]:
#                     l = mid+1
#                 else:
#                     r = mid-1
#             x = difficulty[:mid+1]
#             work_def[worker[i]] = x
        
#         ans = 0
#         for i in range(len(worker)):
#             ans += def_pro[max(work_def[worker[i]])]
#         return ans