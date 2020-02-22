class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        #二维DP
        if not matrix:
            return 0
        m,n = len(matrix), len(matrix[0])
        dp = [[0 if matrix[i][j] == '0' else 1 for j in range(0,n)] for i in range(0,m)]
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = 0
        res = max(max(row) for row in dp)
        return res ** 2
        
        
        
#         n,m = len(matrix), len(matrix[0])
#         if n == 0 or m == 0:
#             return 0
#         maxf = 0
#         size = [[0] * m] * n
#         print(size)
#         for i in range(m):
#             if matrix[0][i] == '1':
#                 matrix[0][i] = 1
#                 size[0][i] = matrix[0][i]
#             else:
#                 matrix[0][i] = 0
#                 size[0][i] = matrix[0][i]
                
#             maxf = max(maxf, size[0][i])
        
#         for j in range(n):
#             if matrix[j][0] == '1':
#                 matrix[j][0] == 1
#             else:
#                 matrix[j][0] == 0
#             size[j][0] = matrix[j][0]
        
#         for r in range(1,n):
#             for c in range(1,m):
#                 if matrix[r][c] == '1':
#                     minf = min(size[r][c-1], size[r-1][c-1])
#                     minf = min(minf, size[r-1][c])
#                     size[r][c] = minf + 1
#                     maxf = max(maxf, size[r][c])
        
#         return maxf^2