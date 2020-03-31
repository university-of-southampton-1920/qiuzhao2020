class Solution:
    def lcs(self, str1, str2):
        dp = [['' for _ in range(len(str2)+1)]for _ in range(len(str1)+1)]
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    dp[i+1][j+1] = dp[i][j] + str1[i]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], key=len)
        return dp[len(str1)][len(str2)]
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        res = ''
        i = 0
        j = 0
        print(self.lcs(str1, str2))
        for c in self.lcs(str1, str2):
            while str1[i] != c:
                res += str1[i]
                i += 1
            while str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i += 1
            j += 1
        return res + str1[i:] + str2[j:]
