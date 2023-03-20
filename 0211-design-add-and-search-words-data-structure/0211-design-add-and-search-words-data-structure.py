class WordDictionary:

    def __init__(self):
        self.children=[None]*26
        self.isCompleteWord=False

    def addWord(self, word: str) -> None:
        cur=self
        for i in word:
            if cur.children[ord(i)-ord('a')]==None:
                cur.children[ord(i)-ord('a')]=WordDictionary()
            cur=cur.children[ord(i)-ord('a')]
        cur.isCompleteWord=True
        

    def search(self, word: str) -> bool:
        cur=self
        for i in range(len(word)):
            c=word[i]
            if c=='.':
                for ch in cur.children:
                    if ch!=None and ch.search(word[i+1:]): return True
                return False
            if cur.children[ord(c)-ord('a')]==None: return False
            cur=cur.children[ord(c)-ord('a')]
        return cur!=None and cur.isCompleteWord

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

