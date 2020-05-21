class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s, p = ' '+ s, ' '+ p
        n = len(s)
        m = len(p)
        dp = [[0]*(m) for _ in range(n)]
        dp[0][0] = 1
        for j in range(1,m):
            if p[j]=='*':
                dp[0][j] = dp[0][j-2]
        for i in range(1,n):
            for j in range(1,m):
                if (s[i]==p[j]) or (p[j]=='.'):
                    dp[i][j] = dp[i-1][j-1]
                elif p[j]=='*':
                    dp[i][j] = dp[i][j-2] or int(dp[i-1][j] and p[j-1] in {s[i], '.'})
                    #if (s[i]==p[j-1]) or (p[j-1]=='.'):
                        #dp[i][j] = dp[i-1][j]
                    #else:
                        #dp[i][j] = dp[i][j-2]
        return bool(dp[-1][-1])