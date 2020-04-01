class Solution:
    def minInsertions(self, s: str) -> int:
        m = len(s)
        dp = [[0]*(m) for _ in range(m)]
        for i in range(m):
            for j in range(i-1,-1,-1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i-1][j+1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j+1])+1
        return dp[-1][0]
                    
