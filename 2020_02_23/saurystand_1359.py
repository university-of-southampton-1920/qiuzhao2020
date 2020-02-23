class Solution:
    def countOrders(self, n: int) -> int:
        res = 1.0
        mod = 1e9 +7
        # for i in range(2, n + 1):
        #     res = res * (i * 2 - 1) * (i * 2) / 2 % mod        
        # return (int) (res)
        dp = [0] * (n+1)
        dp[1] = 1
        if n == 1: return 1
        for i in range(2, n+1):
            pos = (i-1) * 2 + 1
            ans = 0
            for j in range(pos):
                ans += (pos - j)
            dp[i] = ans * dp[i-1] % mod
        return (int) (dp[n] % mod) 



# class Solution:
#     def countOrders(self, n: int) -> int:
#         dp = [0 for i in range(n + 1)]
#         dp[1] = 1
#         mod = 10**9 + 7
#         for i in range(2, n+1):
#             r = (i - 1)*2 + 1
#             rr = int(r * (r + 1) / 2)
#             dp[i] = (rr * dp[i-1]) % mod
#         return dp[n]