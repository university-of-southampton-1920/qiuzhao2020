import heapq
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        #dp + heap
        rows,cols = len(arr), len(arr[0])
        dp = [[None for x in range(rows)] for x in range(cols)]
        dp[0] = arr[0][:]
        for i in range(1,rows):
            lst = [(val, j) for j, val in enumerate(dp[i-1])]
            heapq.heapify(lst)
            val1,j1 = heapq.heappop(lst)
            val2,j2 = heapq.heappop(lst)
            for j in range(cols):
                if j == j1:
                    dp[i][j] = val2 + arr[i][j]
                else:
                    dp[i][j] = val1 + arr[i][j]
        
        return min(dp[-1])
        # for i in range(rows):
        #     for j in range(cols):
        #         dp[i][j] = 1
        # minv = float('inf')
        # for j in range(cols):
        #     minv = min(minv, self.func(arr,rows,cols,0,j,dp))
        # return minv
    
        
        
        
#     def func(self, arr, rows, cols, i, k, dp):
#         if i == 0: return 0
#         if dp[i][k] != -1:
#             return dp[i][k]
#         minv = float('inf')
#         for j in range(cols):
#             if j == k: 
#                 continue
#             minv = min(minv, func(arr,rows, cols, i+1, j, dp))
#         if minv != float('inf'):
#             minv += arr[i][k]
        
#         dp[i][k] = minv
#         return dp[i][k]        
                










# import heapq
# class Solution:
#     def minFallingPathSum(self, arr: List[List[int]]) -> int:
#         row, col = len(arr), len(arr[0])
#         dp = [[10**8 for i in range(col)] for j in range(row)]
#         for i in range(col):
#             dp[0][i] = (arr[0][i],i)
#         for i in range(1, row):
#             q = heapq.nsmallest(2, dp[i-1])
#             for j in range(col):
#                 dp[i][j] = (arr[i][j] + q[0][0] if q[0][1] != j else arr[i][j] + q[1][0], j)
        
#         return min(dp[row-1])[0]