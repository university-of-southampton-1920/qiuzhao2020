class Solution:
    def countOrders(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        mod = 10**9 + 7
        for i in range(2, n+1):
            r = (i - 1)*2 + 1
            rr = int(r * (r + 1) / 2)
            dp[i] = (rr * dp[i-1]) % mod
        return dp[n]