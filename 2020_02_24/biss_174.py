class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row, col = len(dungeon), len(dungeon[0])
        dp = [[-10**8 for j in range(col+1)] for i in range(row+1)]
        dp[row][col-1] = 0
        dp[row-1][col] = 0
        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                dp[i][j] = min( dungeon[i][j] + max(dp[i+1][j], dp[i][j+1]), 0 )
        return abs(dp[0][0]) + 1