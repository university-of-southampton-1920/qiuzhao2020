import numpy as np
class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        dp = [[0 for _ in range(len(A))] for _ in range(len(A))]
        for step in range(2, len(A)):
            for i in range(len(A)):
                if i + step >= len(A):
                    break
                dp[i][i+step] = np.inf
                for j in range(i+1, i+step):
                    dp[i][i+step] = min(dp[i][i+step], dp[i][j]+dp[j][i+step]+A[i]*A[i+step]*A[j])
        return dp[0][-1]
