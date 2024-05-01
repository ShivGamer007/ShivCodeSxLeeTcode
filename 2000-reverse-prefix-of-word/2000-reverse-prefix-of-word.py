class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = ""
        for i in range(len(word)):
            if word[i] == ch:
                ans = ch + word[:i][::-1] + word[i+1:]
                return ans
        return word