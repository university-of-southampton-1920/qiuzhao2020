class Solution:
    def numOfArrays(self, n: int, m: int, K: int) -> int:
        dp = [[[0 for k in range(K+1)] for j in range(m+1)] for i in range(n)]
        M = 10**9 + 7
        for t in range(1, m+1):
            dp[0][t][1] = 1
        for i in range(n):
            for j in range(1, m+1):
                for k in range(1, K+1):
                    # arr[i] == j
                    for t in range(1, j):
                        dp[i][j][k] += dp[i-1][t][k-1]
                    dp[i][j][k] = (dp[i][j][k] +  (dp[i-1][j][k] * j)) % M
        res = 0
        for t in range(1, m+1):
            res = (res + dp[n-1][t][K]) % M
        return res