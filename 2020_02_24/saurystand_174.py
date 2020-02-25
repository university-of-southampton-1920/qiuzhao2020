class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        '''
        The trick is where is the Starting point. 
        This problem ask us to find the least hp in top-left. So in the most optimistic situation, 
        bottom-right value can be determined as 1. Then bottom-right is the starting point.
        '''
#         dlen = len(dungeon)
#         if dlen == 0:
#             return 1
#         nrow = dlen
#         ncol = len(dungeon[0])
#         row = [0] * (ncol + 1)
#         row[ncol-1] = 1
#         i = nrow - 1
#         while i >= 0:
#             j = ncol - 1
#             while j >= 0:
#                 t = min(row[j], row[j + 1]) - dungeon[i][j]
#                 row[j] = max(t, 1)
#                 j -= 1
#             i -= 1
        
#         return row[0]

#         if len(dungeon) == 0 or dungeon == None or len(dungeon[0]) == 0:
#             return 1
#         m,n = len(dungeon),len(dungeon[0])
#         dp = [[0] * (n+1)] * (m + 1)
#         for i in range(m-1,-1,-1):
#             for j in range(n-1,-1,-1):
#                 minhp = min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j]
#                 if minhp <= 0:
#                     dp[i][j] = 1
#                 else:
#                     dp[i][j] = minhp
#         #return max(1, dp[0][0] - dungeon[0][0])
#         return dp[0][0]
        
        if not dungeon:
            return 
        r, c = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[-1][-1] = max(1, 1-dungeon[-1][-1])
        for i in range(c-2, -1, -1):
            dp[-1][i] = max(1, dp[-1][i+1]-dungeon[-1][i])
        for i in range(r-2, -1, -1):
            dp[i][-1] = max(1, dp[i+1][-1]-dungeon[i][-1])
        for i in range(r-2, -1, -1):
            for j in range(c-2, -1, -1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-dungeon[i][j])
        return dp[0][0]
        
        
        