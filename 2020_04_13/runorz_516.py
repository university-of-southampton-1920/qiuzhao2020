class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for step in range(1, len(s)):
            for i in range(len(s)):
                if i + step >= len(s):
                    break
                if s[i] == s[i+step]:
                    dp[i][i+step] = dp[i+1][i+step-1] + 2
                else:
                    dp[i][i+step] = max(dp[i][i+step-1], dp[i+1][i+step])
        return dp[0][-1]
