class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        modulo = 10**9 + 7
        dp = [[0 for _ in range(7)] for _ in range(n)]
        for i in range(6):
            dp[0][i] = 1
        dp[0][6] = 6
        for i in range(1, n):
            s = 0
            for j in range(6):
                dp[i][j] = dp[i-1][6]
                if i - rollMax[j] < 0:
                    s = (s + dp[i][j]) % modulo
                else:
                    if i - rollMax[j] -1 < 0:
                        dp[i][j] = (dp[i][j]-1) % modulo
                    else:
                        dp[i][j] = (dp[i][j] - (dp[i-rollMax[j]-1][6] - dp[i-rollMax[j]-1][j])) % modulo
                    s  = (s + dp[i][j]) % modulo
            dp[i][6] = s
        
        return dp[n-1][6]
