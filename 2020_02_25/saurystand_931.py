
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        rows = len(A)
        cols = len(A[0])
#         # DP matrix has 2 extra columns
#         # dp = [[0] * rows] * (cols + 2)
#         # for i in range(1,cols):
#         #     dp[0][i] = A[0][i]
#         # for i in range(rows):
#         #     dp[i][0] = 0
#         #     dp[i][cols] = 0
#         dp = [[[10**8] for i in range(cols)] for j in range(rows)]
#         for i in range(rows):
#             dp[0][i] = A[0][i]
        
#         for i in range(rows):
#             for j in range(cols):
#                 minNeighbor = min(dp[i-1][j-1], dp[i-1][j])
#                 minNeighbor = min(minNeighbor, dp[i-1][j+1])
#                 dp[i][j] = A[i][j-1] + [minNeighbor]
        
#         minv = 0
#         for i in range(1,cols):
#             minv = min(minv, dp[rows-1][i])
#         return minv
        dp = [[float('inf') for x in range(rows)] for x in range(cols)]
        dp[0][0] = A[0][0]
        for i in range(1,rows):
            dp[0][i] = A[0][i]
        
        for i in range(1,rows):
            for j in range(cols):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + A[i][j]
                elif j == cols-1:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + A[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1], dp[i-1][j-1]) + A[i][j]
                    
        return min(dp[-1])
                    








# class Solution:
#     def minFallingPathSum(self, A: List[List[int]]) -> int:
#         dp = [[10**8 for i in range(len(A[0]))] for j in range(len(A))]
#         for i in range(len(A[0])):
#             dp[0][i] = A[0][i]
#         for row in range(1, len(A)):
#             for col in range(len(A[0])):
#                 if col - 1 >= 0:
#                     dp[row][col] = min(dp[row][col], dp[row-1][col-1])
#                 if col + 1 < len(A[0]):
#                     dp[row][col] = min(dp[row][col], dp[row-1][col+1])
#                 dp[row][col] = min(dp[row][col], dp[row-1][col]) + A[row][col]
#         res = 10**8
#         for i in range(len(A[0])):
#             res = min(res, dp[len(A)-1][i])
#         return res