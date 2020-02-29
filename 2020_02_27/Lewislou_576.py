class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        def dp(i, j, N):
            if i < 0 or i >= m or j < 0 or j >= n:
                return int(N >= 0)
            elif N < 0:
                return 0
            res = 0
            for k in (1, -1):
                res += dp(i + k, j, N - 1) + dp(i, j + k, N - 1)
            return res

        return dp(i, j, N) % (10 ** 9 + 7)
        