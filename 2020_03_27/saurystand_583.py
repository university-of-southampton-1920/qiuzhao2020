class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        s = word1
        t = word2
        dp = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = i
        for i in range(len(t) + 1):
            dp[0][i] = i
        s = "&" + word1
        t = "&" + word2
        for i in range(1, len(s)):
            for j in range(1, len(t)):
                if s[i] == t[j]:  # key point
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[len(s) - 1][len(t) - 1]

