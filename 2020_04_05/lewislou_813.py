class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        dp = [[0]*(K+1) for _ in range(n+1)]

        s = [[0]*(n+1) for _ in range(n+1)]
        for lo in range(n-1, -1, -1):
            for hi in range(lo+1, n+1):
                s[lo][hi] = s[lo+1][hi] + A[lo]

        for i in range(1, n+1):
            dp[i][1] = s[0][i]/i
            for k in range(2, K+1):
                dp[i][k] = max(dp[i][k], 
                               max(dp[j][k-1] + s[j][i]/(i-j) for j in range(i)))
        return dp[n][K]