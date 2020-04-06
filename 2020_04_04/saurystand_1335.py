class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        #         n = len(jobDifficulty)
        #         inf = float('inf')
        #         if n < d:
        #             return -1
        #         #dp = [[inf] * n + [0] for i in range(d + 1)]
        #         dp = [[0 for _ in range(n)] for _ in range(d)]
        #         dp[0][0] = jobDifficulty[0]
        #         for i in range(1, n):
        #             dp[0][i] = max(jobDifficulty[i], dp[0][i-1])

        #         for i in range(1, d):
        #             for j in range(i, n):
        #                 localMax = jobDifficulty[j]
        #                 dp[i][j] = 0
        #                 for r in range(j, i, -1):
        #                     localMax = max(localMax, jobDifficulty[r])
        #                     dp[i][j] = min(dp[i][j], dp[i-1][r-1] + localMax)

        #         return dp[d-1][n-1]

        n = len(jobDifficulty)
        inf = float('inf')
        dp = [inf] * n + [0]
        if n < d:
            return -1
        for d in range(1, d + 1):
            for i in range(n - d + 1):
                maxd, dp[i] = 0, inf
                for j in range(i, n - d + 1):
                    maxd = max(maxd, jobDifficulty[j])
                    dp[i] = min(dp[i], maxd + dp[j + 1])
        return dp[0]