class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        dp = [[''] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 1]

        i, j = 0, 0
        ans = ''
        lcs = dp[m][n]
        for curr in lcs:
            while i < m and curr != str1[i]:
                ans += str1[i]
                i += 1
            while j < n and curr != str2[j]:
                ans += str2[j]
                j += 1
            ans += curr
            i += 1
            j += 1
        ans += str1[i:] + str2[j:]
        return ans