class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        if not board:
            return [0,0]
        # dp[i][j][0] is the max value from 'S' to this cell
        # dp[i][j][1] is the number of paths
        n, mod = len(board), pow(10,9) + 7
        dp = [[[-1, 0] for _ in range(n+1)] for _ in range(n+1)]
        dp[0][0] = [0,0]
        dp[n-1][n-1] = [0,1]
        # loop bottom-to-up, right-to-left
        for i in range(n)[::-1]:
            for j in range(n)[::-1]:
                if board[i][j] in 'XS':
                    continue
                for tx,ty in ((1,0),(0,1),(1,1)):
                    x,y = i + tx, j + ty
                    if dp[i][j][0] < dp[x][y][0]:
                        dp[i][j] = [dp[x][y][0], 0]
                    if dp[i][j][0] == dp[x][y][0]:
                        dp[i][j][1] += dp[x][y][1]
                        dp[i][j][1] %= mod
                
                # if there exits some path from 'E' to current position, update info of current position
                if dp[i][j][0] != -1 and (i or j):
                    dp[i][j][0] += int(board[i][j])
                    dp[i][j][0] %= mod
        return dp[0][0]
            


# class Solution:
#     def pathsWithMaxScore(self, board: List[str]) -> List[int]:
#         row, col = len(board), len(board[0])
#         dp = [[0 for j in range(col)] for i in range(row)]
#         # initialization
#         dp[0][0] = (0, 1)
#         mod = 10**9 + 7
#         for i in range(1, row):
#             if board[i][0] != "X" and dp[i-1][0][0] != -1:
#                 dp[i][0] = (dp[i-1][0][0] + int(board[i][0]), dp[i-1][0][1] )
#             else:
#                 dp[i][0] = (-1, -1)
#         for i in range(1, col):
#             if board[0][i] != "X" and dp[0][i-1][0] != -1:
#                 dp[0][i] = (dp[0][i-1][0]+int(board[0][i]), dp[0][i-1][1] )
#             else:
#                 dp[0][i] = (-1, -1)
#         # cal dp
#         for i in range(1, row):
#             for j in range(1, col):
#                 if board[i][j] == "X" or board[i][j] == "S":
#                     t = 0
#                 else:
#                     t = int(board[i][j])
                
#                 if board[i][j] == "X":
#                     dp[i][j] = (-1, -1)
#                 elif (dp[i-1][j][0] == -1 and dp[i][j-1][0] == -1 ):
#                     if board[i-1][j-1] != "X":
#                         dp[i][j] = (dp[i-1][j-1][0] + t, dp[i-1][j-1][1] )
#                     else:
#                         dp[i][j] = (-1, -1)
#                 else:
#                     if dp[i-1][j][0] == dp[i][j-1][0]:
#                         dp[i][j] = ( dp[i-1][j][0]+ t, dp[i-1][j][1] + dp[i][j-1][1] )
#                     else:
#                         if dp[i-1][j][0] > dp[i][j-1][0]:
#                             dp[i][j] = ( dp[i-1][j][0]+ t, dp[i-1][j][1] )
#                         else:
#                             dp[i][j] = ( dp[i][j-1][0] + t, dp[i][j-1][1] )
#                 # mod
#                 dp[i][j] = (dp[i][j][0] % mod, dp[i][j][1]%mod) if dp[i][j][0] >= 0 else dp[i][j]
#         return list(dp[row-1][col-1]) if dp[row-1][col-1][0] != -1 else [0, 0]