class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 0:
            return 0
        if L == 1:
            return nums[0]
        dp = [0 for i in range(L)]
        # rob the first one
        dp[0] = nums[0]
        res = dp[0]
        for i in range(2, L-1):
            for j in range( i-1):
                dp[i] = max(dp[i], dp[j] + nums[i])
                res = max(res, dp[i])
        # do not rob the first one
        dp = [0 for i in range(L)]
        dp[1] = nums[1]
        res = max(res, dp[1])
        for i in range(2, L):
            for j in range(i-1):
                dp[i] = max(dp[i], dp[j] + nums[i])
                res = max(res, dp[i])
        return res