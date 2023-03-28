class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp=[0]*366
        traveldays=set()
        for day in days:
            traveldays.add(day)
        for i in range(366):
            if i not in traveldays:
                dp[i]=dp[i-1]
            else:
                dp[i]=min(dp[i-1]+costs[0],min(dp[max(0,i-7)]+costs[1],dp[max(0,i-30)]+costs[2]))
        return dp[365]
        
        