from collections import Counter
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [Counter() for i in range(len(A))]
        res = 0
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if dp[j][diff] == 0:
                    dp[i][diff] = 2
                else:
                    dp[i][diff] = dp[j][diff] + 1
                res = max(res, dp[i][diff])
        return res