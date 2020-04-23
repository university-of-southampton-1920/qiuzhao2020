class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        L = len(A)
        INT_MAX = 10**8
        dp = [[INT_MAX for i in range(L)] for j in range(L)]
        for i in range(L-1):
            dp[i][i+1] = 0
        for l in range(2, L):
            for i in range(L-l):
                j = i + l
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k]+A[i]*A[k]*A[j]+dp[k][j])
        return dp[0][L-1]