class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split(" ")
        for i in range(len(ss)):
            ss[i] = ss[i][::-1]
            
        return " ".join(ss)