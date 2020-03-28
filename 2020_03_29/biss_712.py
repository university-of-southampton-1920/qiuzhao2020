class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        s1 = "$" + s1
        s2 = "$" + s2
        dp = [[0 for i in range(len(s2))] for j in range(len(s1))]
        for i in range(1, len(s1)):
            dp[i][0] = dp[i-1][0] + ord(s1[i])
        for i in range(1, len(s2)):
            dp[0][i] = dp[0][i-1] + ord(s2[i])
            
        for i in range(1, len(s1)):
            for j in range(1, len(s2)):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i]), 
                                  dp[i][j-1] + ord(s2[j]),
                                  dp[i-1][j-1] + ord(s1[i]) + ord(s2[j]))
        return dp[len(s1)-1][len(s2)-1]