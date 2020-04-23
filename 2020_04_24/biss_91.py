class Solution:
    def numDecodings(self, s: str) -> int:
        mark = [str(i) for i in range(1, 27)]
        dp = [0 for i in range(len(s)+1)]
        s = "&" + s
        dp[0] = 1
        for i in range(1, len(s)):
            for m in mark:
                j = i - len(m) + 1
                if s[j:i+1] == m:
                    dp[i] += dp[j-1]
        return dp[len(s)-1]