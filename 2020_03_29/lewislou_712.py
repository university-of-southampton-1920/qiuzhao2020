class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m,n = len(s1),len(s2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            dp[i][0] = dp[i-1][0]+ord(s1[i-1])
        for i in range(1,n+1):
            dp[0][i] = dp[0][i-1]+ord(s2[i-1])
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j]
                    
                else:
                    dp[i+1][j+1] = min(dp[i][j+1]+ord(s1[i]),dp[i+1][j]+ord(s2[j]))
        return dp[-1][-1]
