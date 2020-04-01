class Solution:
    def minInsertions(self, s: str) -> int:
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        s1 = s
        s2 = s[::-1]
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return len(s) - dp[len(s)][len(s)]
