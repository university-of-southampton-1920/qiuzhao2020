class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [0 for _ in range(len(A))]
        for i in range(len(A)):
            m = 0
            for j in range(1, K+1):
                if i - j + 1 >= 0:
                    m = max(m, A[i-j+1])
                    dp[i] = max(dp[i], (dp[i-j] if i >= j else 0) + m*j)
        return dp[-1]
