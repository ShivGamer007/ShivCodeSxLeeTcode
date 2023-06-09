class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = '~'
        for i in range(len(letters)):
            if letters[i] > target:
                ans = min(ans, letters[i])
        if ans == '~':
            return letters[0]
        return ans