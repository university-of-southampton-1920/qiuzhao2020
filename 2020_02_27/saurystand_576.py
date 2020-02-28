class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # explaination
        # https://buptwc.com/2018/07/19/Leetcode-576-Out-of-Boundary-Paths/
        mod = 10**9 + 7
        cache = collections.defaultdict(int)
        def helper(i,j,N):
            # 记忆思想
            if (i,j,N) in cache:
                return cache[(i,j,N)]
            # i,j在网格内
            if 0 <= i < m and 0 <= j < n:
                if N==0:
                    cache[(i,j,N)] = 0
                    return cache[(i,j,N)]
                listc = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
                for x,y in listc:
                    cache[i,j,N] += helper(x,y,N-1)
                return cache[(i,j,N)] % mod
            else:
                #网格外
                cache[i,j,N] = 1
                return cache[(i,j,N)]
        return helper(i,j,N) % mod
        #dfs会超时



# class Solution:
#     def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
#         dp = [ [0 for i in range(n)] for j in range(m)] # dp indicate dp[i][j] have time N left to go out of the grid
#         r = i
#         c = j
#         mod = 10**9 + 7
#         for t in range(N):
#             tmp = [ [dp[j][i] for i in range(n)] for j in range(m)]
#             for i in range(m):
#                 for j in range(n):
#                     tmp[i][j] += dp[i-1][j] if i-1>=0 else 1
#                     tmp[i][j] += dp[i+1][j] if i+1<m else 1
#                     tmp[i][j] += dp[i][j-1] if j-1>=0 else 1
#                     tmp[i][j] += dp[i][j+1] if j+1<n else 1
#                     tmp[i][j] =  (tmp[i][j] - dp[i][j]) % mod
#             dp = tmp
#             print(dp)
#         return dp[r][c]