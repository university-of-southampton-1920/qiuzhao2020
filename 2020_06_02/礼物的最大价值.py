class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])
        cur = grid[0]
        for j in range(1,n):
            cur[j] = cur[j-1] + cur[j]
        for i in range(1,m):
            pre = cur       
            for j in range(n):
                if j == 0:
                    cur[j] = pre[j] + grid[i][j]
                elif cur[j-1] > pre[j]:
                    cur[j] = cur[j-1] + grid[i][j]
                else:
                    cur[j] = pre[j] + grid[i][j]
        return cur[-1]
                