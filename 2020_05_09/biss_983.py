class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [10**8 for i in range(366)]
        dp[0] = 0
        day_set = set(days)
        for i in range(1, 366):
            if i not in day_set:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i], dp[max(0, i-1)]+costs[0])
                dp[i] = min(dp[i], dp[max(0, i-7)]+costs[1])
                dp[i] = min(dp[i], dp[max(0, i-30)]+costs[2])
        return dp[-1]