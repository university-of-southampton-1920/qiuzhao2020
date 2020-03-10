class Solution:
    def knightDialer(self, N: int) -> int:
#         map_dict = {(4,6), (7,9),(0,3,9),(),(0,1,7),(2,6),(1,3),(2,4)}
#         memo = [[0] * 10] * (N+1)
#         for i in range(N):
#             memo[i] = -1
#         result = 0
#         for i in range(10):
#             result += self.helper(N, i, map_dict, memo)
#             result %= (int) (1e9 + 7)
#         return result
    
#     def helper(self, N, start, map_dict, memo):
#         if N == 1: return 1
#         if memo[N][start] > -1:
#             return memo[N][start]
#         memo[N][start] = 0
#         for m in map_dict[start]:
#             memo[N][start] += helper(N-1, m, map_dict, memo)
#             memo[N][start] %= (int) (1e9 + 7)
#         return memo[N][start]
        dct = {1:[6, 8], 2:[7, 9], 3:[4, 8], 4:[0, 3, 9], 5:[], 6:[0, 1, 7], 7:[2, 6], 8:[1, 3], 9:[2, 4], 0:[4, 6]}
        dp = [1] * 10
        for _ in range(N-1):
            nxt = [0] * 10
            for i in range(10):
                for j in dct[i]:
                    nxt[j] += dp[i]
            dp = nxt
        #return sum(dp) % (1e9 + 7)
        return sum(dp) % (10 ** 9 + 7)



# class Solution:
#     def knightDialer(self, N):
#         x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 1
#         for i in range(N - 1):
#             x1, x2, x3, x4, x5, x6, x7, x8, x9, x0 = x6 + x8, x7 + x9, x4 + x8, x3 + x9 + x0, 0, x1 + x7 + x0,x2 + x6, x1 + x3, x2 + x4, x4 + x6
#         return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % (10**9 + 7)
