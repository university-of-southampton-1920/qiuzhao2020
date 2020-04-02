class Solution:
    def palindromePartition(self, s: str, K: int) -> int:
        s = "$" + s
        count = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(1, len(s)-1):
            count[i][i+1] = 1 if s[i] != s[i+1] else 0
        for l in range(1, len(s)):
            for i in range(1, len(s)-l):
                j = i + l
                if s[i] == s[j]:
                    count[i][j] = count[i+1][j-1]
                else:
                    count[i][j] = count[i+1][j-1] + 1
        dp = [[10**8 for i in range(K+1)] for j in range(len(s))]
        dp[0][0] = 0
        for i in range(1, len(s)):
            for k in range(1, K+1):
                if k>i:
                    break
                for j in range(1, i+1):
                    dp[i][k] = min(dp[i][k], dp[j-1][k-1]+count[j][i])
        # for i in dp:
        #     print(i)
        return dp[len(s)-1][K]