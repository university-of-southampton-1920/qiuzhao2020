class Solution:
    def numDecodings(self, s: str) -> int:
        s = "&" + s
        dp = [0 for i in s]
        Z = [str(i) for i in range(1, 27)]
        M = 10**9 + 7
        dp[0] = 1
        for i in range(1, len(s)):
            for z in Z:
                j = i- len(z) + 1
                if z == s[j:i+1]:
                    dp[i] += dp[j-1]
                elif s[i] == "*":
                    if z == "10" or z=="20":
                        continue
                    if len(z) == 1:
                        dp[i] += dp[j-1]
                    else:
                        dp[i] += dp[j-1] if s[i-1] == "*" or s[j] == z[0] else 0
                elif j!=i and s[j] == "*":
                    if s[i] == z[1]:
                        dp[i] += dp[j-1]
            dp[i] %= M
        return dp[len(s)-1]
                            