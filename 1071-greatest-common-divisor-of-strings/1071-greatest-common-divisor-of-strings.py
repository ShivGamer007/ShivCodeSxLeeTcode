class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        x=""
        # n=min(len(str1),len(str2))
        # for i in range(n):
        #     if str1[i]==str2[i]:
        #         x+=str1[i]
        #     else:
        #         break
        # return x
        if str1+str2==str2+str1:
            x=str1[:gcd(len(str1),len(str2))]
        return x