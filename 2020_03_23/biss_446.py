from collections import Counter
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # dp = [Counter() for i in range(len(A))]
        # res = 0
        # for i in range(1, len(A)):
        #     for j in range(i):
        #         diff = A[i] - A[j]
        #         dp[i][diff] += dp[j][diff] + 1
        #         res += dp[j][diff]
        
        res = 0
        dp = [Counter() for i in range(len(A))]
        for i in range(1, len(A)):
            for j in range(i):
                k = A[j] - (A[i]-A[j])
                dp[i][A[j]] += dp[j][k] + 1
                res += dp[j][k]
        return res

# dp[i] = dp[i-1]

# 2, 4, 6, 6, 8
# dp[i-1] = 2
# dp[i][diff] += dp[i-1][diff] + 1
# diff = A[i] - A[i-1]

# dp[i][j] = dp[j][k] + 1