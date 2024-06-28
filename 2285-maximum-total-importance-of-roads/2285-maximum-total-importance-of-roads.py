class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        arr = [0] * (n)
        for road in roads:
            arr[road[0]] += 1
            arr[road[1]] += 1
        ans = 0
        arr.sort(reverse = True)
        # print(arr)
        for i in range(len(arr)):
            ans += arr[i] * n
            n -= 1
        return ans