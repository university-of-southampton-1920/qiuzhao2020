class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        dp = [[10**8 for i in range(len(A[0]))] for j in range(len(A))]
        for i in range(len(A[0])):
            dp[0][i] = A[0][i]
        for row in range(1, len(A)):
            for col in range(len(A[0])):
                if col - 1 >= 0:
                    dp[row][col] = min(dp[row][col], dp[row-1][col-1])
                if col + 1 < len(A[0]):
                    dp[row][col] = min(dp[row][col], dp[row-1][col+1])
                dp[row][col] = min(dp[row][col], dp[row-1][col]) + A[row][col]
        res = 10**8
        for i in range(len(A[0])):
            res = min(res, dp[len(A)-1][i])
        return res