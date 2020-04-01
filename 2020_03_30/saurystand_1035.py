# The Longest Common Subsequence
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for i in range(len(B) + 1)] for j in range(len(A) + 1)]
        a, b = len(A), len(B)
        for i in range(1, a + 1):
            for j in range(1, b + 1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[a][b]
