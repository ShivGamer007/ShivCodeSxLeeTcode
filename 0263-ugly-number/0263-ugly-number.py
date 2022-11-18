class Solution:
    
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        while(n%2==0):
            n=n/2
        while(n%3)==0:
            n=n/3
        while(n%5)==0:
            n=n/5
        if n==1:
            return True
        else:
            return False
        
        
#         prime=[]
#         for i in range(n):
#             if i%
        
        
#         x=prime_factors(n)
#         if 
    
#     public:   
        
#     def prime_factors(n):
#         fs=[]
#         while(n%2==0):
#             fs.append(2)
#             n=n//2;
#         for i in range(3,sqrt(n),2):
#             while(n%i==0):
#                 fs.append(i)
#                 n=n//i
#         if n>2:
#             fs.append(n)