class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        x=[]
        for i in s:
            x.append(i)
        n=len(x)
        s1=x[:n//2]
        s2=x[n//2:]
        c1,c2=0,0
        vowels=['a','e','i','o','u','A','E','I','O','U']
        for i in s1:
            if i in vowels:
                c1+=1
        for i in s2:
            if i in vowels:
                c2+=1
        if c1==c2:
            return True
        return False