class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [0 for i in range(len(A))]
        dp[0] = A[0]
        for i in range(1, len(A)):
            maxv = A[i]
            for j in range(i-1, max(-2, i-K-1), -1):
                if j > -1:
                    dp[i] = max(dp[i], dp[j] + maxv*(i-j))
                    maxv = max(maxv, A[j])
                elif j == -1:
                    dp[i] = max(dp[i], maxv*(i-j))
                    
        return dp[len(A)-1]