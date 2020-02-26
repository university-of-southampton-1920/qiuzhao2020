import heapq
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        row, col = len(arr), len(arr[0])
        dp = [[10**8 for i in range(col)] for j in range(row)]
        for i in range(col):
            dp[0][i] = (arr[0][i],i)
        for i in range(1, row):
            q = heapq.nsmallest(2, dp[i-1])
            for j in range(col):
                dp[i][j] = (arr[i][j] + q[0][0] if q[0][1] != j else arr[i][j] + q[1][0], j)
        
        return min(dp[row-1])[0]