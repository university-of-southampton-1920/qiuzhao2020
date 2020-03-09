class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        s = sum(nums)
        if S < -s or S > s:
            return 0
        dp = [[0 for _ in range(2*s + 1)] for _ in range(len(nums)+1)]
        dp[0][s] = 1
        for i in range(1,len(nums)+1):
            for j in range(2*s + 1):
                if j + nums[i-1] < 2*s+1:
                    dp[i][j] +=dp[i-1][j+nums[i-1]]
                if j - nums[i-1] >= 0:
                    dp[i][j] += dp[i-1][j-nums[i-1]]
        return dp[len(nums)][s+S]
