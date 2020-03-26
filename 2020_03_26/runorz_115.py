class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[1 if j==0 else 0 for i in range(len(s)+1)] for j in range(len(t)+1) ]
        for i in range(len(t)):
            for j in range(len(s)):
                if s[j] == t[i]:
                    dp[i+1][j+1] = dp[i][j] + dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j]
        return dp[len(t)][len(s)]
