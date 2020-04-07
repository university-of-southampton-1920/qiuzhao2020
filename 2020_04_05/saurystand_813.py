class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        curr = 0
        for i in range(n):
            curr += A[i]
            dp[i + 1][1] = curr / (i + 1)
        return self.search(n, K, A, dp)

    def search(self, n, K, A, dp):
        if dp[n][K] > 0: return dp[n][K]
        if n < K: return 0
        curr = 0
        for i in range(n - 1, 0, -1):
            curr += A[i]
            dp[n][K] = max(dp[n][K], self.search(i, K - 1, A, dp) + curr / (n - i))
        return dp[n][K]