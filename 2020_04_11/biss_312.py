class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for l in range(len(nums)-2):
            for i in range(1, len(nums)-1-l):
                j = i + l
                for k in range(i, j+1):
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + dp[k+1][j] + nums[k] * nums[i-1] * nums[j+1])
        return dp[1][len(nums)-2]