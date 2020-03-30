class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        s1 = "$" + str1
        s2 = "$" + str2
        dp = [[ 0 for i in range(len(s2)) ] for j in range(len(s1))]
        for i in range(1, len(s1)):
            dp[i][0] = dp[i-1][0] + 1
        for i in range(1, len(s2)):
            dp[0][i] = dp[0][i-1] + 1
        for i in range(1, len(s1)):
            for j in range(1, len(s2)):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        i, j = len(s1)-1, len(s2)-1
        res = ''
        while i > 0 and j > 0:
            if s1[i] == s2[j]:
                res += s1[i]
                i-=1
                j-=1
            else:
                if dp[i-1][j] < dp[i][j-1]:
                    res += s1[i]
                    i-=1
                else:
                    res += s2[j]
                    j-=1
        while i>0:
            res += s1[i]
            i-=1
        while j >0:
            res += s2[j]
            j-=1
        return "".join(list(reversed(res)))