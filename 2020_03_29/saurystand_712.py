class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)] # m*n
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j] + ord(s1[i])
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        sm = sum([ord(s) for s in s1])
        sn = sum([ord(s) for s in s2])
        return sm-dp[m][n] + sn-dp[m][n]
        # # for i in range(m+1):
        # #     dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        # # for j in range(n+1):
        # #     dp[0][j] = dp[0][j-1] + ord(s2[j-1])
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         if s1[i-1] == s2[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        # return dp[m][n]