class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def calculate(i, j):
            if dp[i][j] or j == i + 1:  # in memory or gap < 2
                return dp[i][j]
            coins = 0
            for k in range(i + 1, j):  # find the last balloon
                coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
            dp[i][j] = coins
            return coins

        return calculate(0, n - 1)

#         if nums is None: return 0
#         newnums = [0] * (len(nums) + 2)
#         n = 1
#         for nn in nums:
#             newnums[n] = nn
#             n += 1
#         newnums[0] = 1
#         newnums[n] = 1

#         dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
#         for k in range(n):
#             for left in range(n-k):
#                 right = left + k
#                 for i in range(left+1, right):
#                     dp[left][right] = max(dp[left][right],
#                     nums[left] * nums[i] * nums[right] + dp[left][i-1] + dp[i-1][right])

#         return dp[0][n-1]

