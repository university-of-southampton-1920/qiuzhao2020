class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [["" for _ in range(len(str1) + 1)] for _ in range(2)]
        for j in range(1, len(str1) + 1):
            dp[0][j] = str1[:j]
        cur = 1
        p = 0
        for i in range(1, len(str2) + 1):
            p = 1-p
            dp[p][0] = str2[:cur]
            cur += 1
            for j in range(1, len(str1) + 1):
                if str2[i-1] == str1[j-1]:
                    dp[p][j] = dp[1 - p][j - 1] + str1[j-1]
                else:
                    if len(dp[1 - p][j]) <= len(dp[p][j - 1]):
                        dp[p][j] = dp[1 - p][j] + str2[i-1]
                    else:
                        dp[p][j] = dp[p][j - 1] + str1[j-1]
        return dp[p][-1]
                        