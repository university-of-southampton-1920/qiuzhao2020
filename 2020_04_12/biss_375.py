class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0 for i in range(n+2)] for j in range(n+2)]
        for i in range(1, n):
            dp[i][i+1] = i
        for l in range(2, n):
            for i in range(1, n+1-l):
                j = i + l
                g = 10**8
                for p in range(i,j+1):
                    g = min(g , max(dp[i][p-1], dp[p+1][j]) + p)
                dp[i][j] = g
        return dp[1][n]