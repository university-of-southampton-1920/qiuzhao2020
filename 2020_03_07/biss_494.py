from collections import Counter
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        rsum = sum(nums)
        dp = [Counter() for i in range(len(nums)+1)]
        dp[0][0] = 1
        nums = [0] + nums
        for i in range(1, len(nums)):
            for s in range(-rsum, rsum+1):
                dp[i][s+nums[i]] += dp[i-1][s]
                dp[i][s-nums[i]] += dp[i-1][s]
        return dp[len(nums)-1][S]