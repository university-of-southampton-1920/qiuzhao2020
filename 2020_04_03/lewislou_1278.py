class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        
        dp = [[10000 + 1] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] if i + 1 < j - 1 else 0
                else:
                    dp[i][j] = 1 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)

        
        @functools.lru_cache(maxsize=None)
        def dpp(i, k):
            if k == 1:
                return dp[0][i]
            if k > i + 1:
                return 10000
            res = 10000
            for j in range(i):
                res = min(res, dpp(j, k -1) + dp[j + 1][i])
            return res
        
        return dpp(len(s) - 1, k)