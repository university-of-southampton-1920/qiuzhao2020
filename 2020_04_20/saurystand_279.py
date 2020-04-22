class Solution:
    def numSquares(self, n: int) -> int:
        # 转移方程要构造出来
        dp = [0] * (n+1)
        for i in range(n+1):
            dp[i] = i
            j = 1
            while i - j*j >= 0:
                dp[i] = min(dp[i], dp[i-j*j] + 1)
                j += 1
        return dp[n]