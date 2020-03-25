class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s = "$"+s
        t = "$"+t
        dp = [[0 for i in range(len(t))] for j in range(len(s))]
        dp[0][0] = 1
        for i in range(len(s)):
            dp[i][0] = 1
        for i in range(1, len(s)):
            for j in range(1, len(t)):
                if s[i] == t[j]:
                    dp[i][j] += dp[i-1][j-1]
                dp[i][j] += dp[i-1][j]
        return dp[len(s)-1][len(t)-1]