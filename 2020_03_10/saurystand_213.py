class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max(self.rob1(nums, 0, n - 2), self.rob1(nums, 1, n - 1))

    def rob1(self, nums, lo, hi):

        preRob = 0
        preNotRob = 0
        rob = 0
        notRob = 0
        for i in range(lo, hi + 1):
            rob = preNotRob + nums[i]
            notRob = max(preRob, preNotRob)
            preNotRob = notRob
            preRob = rob
        return max(rob, notRob)
#         n = len(nums)
#         if n == 0:
#             return 0
#         if n == 1:
#             return nums[0]
#         tmp = nums[0]
#         nums[0] = 0
#         res = self.rob1(nums)
#         nums[0] = tmp
#         nums[n-1] = 0
#         return max(res, self.rob1(nums))


#     def rob1(self, nums):
#         n = len(nums)
#         dp = [[0] * 2] * (n+1)
#         for i in range(1, n):
#             dp[0][i] = max(dp[0][i-1], dp[1][i-1])
#             dp[1][i] = nums[i-1] + dp[0][i-1]
#         return max(dp[0][n], dp[1][n])