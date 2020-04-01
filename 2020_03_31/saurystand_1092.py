class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str1 += "$"
        str2 += "$"
        dp = [[0 for i in range(len(str2))] for j in range(len(str1))]
        m, n = len(str1), len(str2)
        for i in range(1, len(str1)):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, len(str2)):
            dp[0][i] = dp[0][i - 1] + 1

        for i in range(1, m):
            for j in range(1, n):
                if str1[i] == str2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
                # if i == 0:
                #     dp[i][j] = j
                # elif j == 0:
                #     dp[i][j] = i
                # elif str1[i-1] == str2[j-1]:
                #     dp[i][j] = dp[i-1][j-1] + 1
                # else:
                #     dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        i, j = m - 1, n - 1
        arr = ''
        while i > 0 and j > 0:
            if str1[i] == str2[j]:
                arr += str1[i]
                i -= 1
                j -= 1
            else:
                if dp[i - 1][j] < dp[i][j - 1]:
                    arr += str1[i]
                    i -= 1
                else:
                    arr += str2[j]
                    j -= 1

        while i > 0:
            arr += str1[i]
            i -= 1
        while j > 0:
            arr += str2[j]
            j -= 1
        return arr
