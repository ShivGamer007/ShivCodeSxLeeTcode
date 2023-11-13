class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A','E','I','O','U','a','e','i','o','u']
        loc = []
        vow = []
        for i in range(len(s)):
            if s[i] in vowels:
                loc.append(i)
                vow.append(s[i])
        vow.sort()
        t = [i for i in s]
        # print(t)
        x = 0
        for i in loc:
            t[i] = vow[x]
            x += 1
        return "".join(t)