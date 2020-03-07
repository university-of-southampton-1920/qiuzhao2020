class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(2, n+1):
            dp[i] = i
            for j in range(i-1, 1, -1):
                if i % j == 0:
                    dp[i] = dp[j] + int(i/j)
                    break
        return dp[n]

# class Solution:
#     def minSteps(self, n: int) -> int:
#         count = 0
#         d = 2
#         while n > 1:
#             while n%d == 0:
#                 count+=d
#                 n /= d
#             d+=1
#         return count
#             