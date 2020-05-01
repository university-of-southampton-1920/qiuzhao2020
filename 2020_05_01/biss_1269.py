class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if arrLen > steps+1:
            arrLen = steps + 1
        dp = [[0 for p in range(arrLen)] for s in range(steps)]
        M = 10**9 + 7
        # start at dp with index 0
        dp[0][0] = 1
        dp[0][1] = 1
        for s in range(1,steps):
            for p in range(arrLen):
                dp[s][p] = dp[s-1][p]
                if p + 1 < arrLen:
                    dp[s][p] += dp[s-1][p+1]
                if p - 1 >= 0:
                    dp[s][p] += dp[s-1][p-1]
                dp[s][p] %= M
        return dp[steps-1][0]