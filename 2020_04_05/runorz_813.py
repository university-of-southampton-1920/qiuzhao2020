class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        a = [[0 for _ in range(len(A))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(i, len(A)):
                a[i][j] = sum(A[i:j+1]) / len(A[i:j+1])
        dp = [[0 for _ in range(len(A))] for _ in range(K+1)]
        for i in range(len(A)):
            dp[1][i] = a[0][i]
        for i in range(2, K+1):
            for j in range(len(A)):
                for q in range(i-2, j):
                    dp[i][j] = max(dp[i][j], dp[i-1][q]+a[q+1][j])
        res = 0
        for i in range(1, K+1):
            res =max(res, dp[i][-1])
        return res
