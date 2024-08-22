class Solution:
    def findComplement(self, num: int) -> int:
        x=[i for i in str(bin(num))[2:]]
        
        # print(x)
        for i in range(len(x)):
            if x[i] == '0':
                x[i] = '1'
            else:
                x[i] = '0'
        return int("".join(x),2)