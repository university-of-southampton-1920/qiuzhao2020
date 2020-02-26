class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = [ [0 for i in range(n)] for j in range(m)] # dp indicate dp[i][j] have time N left to go out of the grid
        r = i
        c = j
        mod = 10**9 + 7
        for t in range(N):
            tmp = [ [dp[j][i] for i in range(n)] for j in range(m)]
            for i in range(m):
                for j in range(n):
                    tmp[i][j] += dp[i-1][j] if i-1>=0 else 1
                    tmp[i][j] += dp[i+1][j] if i+1<m else 1
                    tmp[i][j] += dp[i][j-1] if j-1>=0 else 1
                    tmp[i][j] += dp[i][j+1] if j+1<n else 1
                    tmp[i][j] =  (tmp[i][j] - dp[i][j]) % mod
            dp = tmp
            print(dp)
        return dp[r][c]