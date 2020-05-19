class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()

        def dp(K, N):
            if K == 1: return N
            if N == 0: return 0
            if (K, N) in memo:
                return memo[(K, N)]

            res = float('inf')
            low, high = 1, N
            while low <= high:
                mid = low + (high - low) // 2

                broken = dp(K - 1, mid - 1)
                notbroken = dp(K, N - mid)
                if broken > notbroken:
                    high = mid - 1
                    res = min(res, broken + 1)
                else:
                    low = mid + 1
                    res = min(res, notbroken + 1)
            memo[(K, N)] = res
            return res

        return dp(K, N)
        # if K == 1: return N
        # if N == 0: return 0
        # #dp = [0 * (N+1)] * (K+1)
        # dp = [[float('inf') for _ in range(N+1)] for _ in range(K+1)]
        # for i in range(1, N):
        #     dp[0][i] = 0
        #     for j in range(1, K):
        #         dp[j][i] = dp[j][i-1] + dp[j-1][i-1] + 1
        #         if dp[j][i] >= N:
        #             return i
        # return N
