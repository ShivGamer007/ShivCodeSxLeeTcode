class LRUCache:

    def __init__(self, capacity: int):
        self.dc = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.dc:
            return -1
        self.dc[key] = self.dc.pop(key)
        return self.dc[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dc:
            self.dc.pop(key)
        else:
            if self.cap:
                self.cap -= 1
            else:
                self.dc.pop(next(iter(self.dc)))
        self.dc[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

