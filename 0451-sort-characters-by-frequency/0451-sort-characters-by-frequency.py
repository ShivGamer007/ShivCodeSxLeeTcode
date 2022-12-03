from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(sorted(s, key=lambda c, freq=Counter(s): (-freq[c],c)))
        #         
# arr=[]
#         for i in s:
#             arr.append(i)
#         x=dict(Counter(arr))
#         # {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
#         p=dict(sorted(x.items(), key=lambda item: item[1],reverse=True))
        
            
#         print(p)
#         dc={}
#         for i in x:
#             dc[i]=x[i]
#         print(dc)
        
#         return s
        # # print(x)
        # p=sorted(x.values())
        # print(p)
        # return s
        
        # return "".join(sorted(s, key=lambda c, freq=Counter(s): (-freq[c],c)))