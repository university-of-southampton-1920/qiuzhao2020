class Solution:
    def minInsertions(self, s: str) -> int:
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        
        for i in range(len(s)-1):
            dp[i][i+1] = 0 if s[i]==s[i+1] else 1
        
        for l in range(2, len(s)):
            for i in range(len(s)-l):
                j = i + l
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1])+1
        return dp[0][len(s)-1]